Using gettext in compiled Qt ui files with PySide
#################################################
:date: 2012-01-23 21:12
:author: s0undt3ch
:slug: using-gettext-in-compiled-qt-ui-files-with-pyside
:url: 2012/01/23/using-gettext-in-compiled-qt-ui-files-with-pyside
:save_as: 2012/01/23/using-gettext-in-compiled-qt-ui-files-with-pyside/index.html
:category: Python
:tags: PySide, Qt
:summary: This recipe is based on the PyQt recipe found `here <http://www.themacaque.com/?p=816>`_.
          This is just the `PySide`_ port of it.

          In some cases you might find yourself in the situation of wanting to use
          gettext in a `PySide`_ project in which you have ``.ui`` files generated using QtDesigner.

          For those kind of situations is a good idea to extend the `PySide`_ compiler.
          The following example shows how to do so in a distutils command.

This recipe is based on the PyQt recipe found `here <http://www.themacaque.com/?p=816>`_.
This is just the `PySide`_ port of it.

In some cases you might find yourself in the situation of wanting to use
gettext in a `PySide`_ project in which you have ``.ui`` files generated using QtDesigner.

For those kind of situations is a good idea to extend the `PySide`_ compiler.
The following example shows how to do so in a distutils command.


.. code-block:: python

   class CompileUI(Command):
       """Build PyQt (.ui) files and resources."""

       description = "build PySide Qt GUIs (.ui)."

       user_options = [
           ('input-dir=', 'i', 'Input directory path where to search \'.ui\' files.'),
           ('output-dir=', 'o', 'Output directory path for the generated UI files.'),
           ('indent=', 'I', 'set indent width to N spaces, tab if N is 0 (default: 4)'),
           ('i18n-module', 'm', 'specify from which module the \'_()\' function '
                                'should be imported. Ex: mymodule.i18n'),
           ('ui-execute', 'x', 'generate extra code to test and display the class'),
           ('from-imports', 'F', 'generate imports relative to \'.\'')
       ]
       boolean_options = ['from-imports', 'ui-execute']

       def initialize_options(self):
           self.input_dir = None
           self.output_dir = None
           self.indent = 4
           self.i18n_module = None
           self.ui_execute = False
           self.from_imports = False

       def finalize_options(self):
           if self.input_dir is None:
               raise DistutilsOptionError("You need to specify the input "
                                          "directory from where to search for the "
                                          "'.ui' files")
           if self.output_dir is None:
               raise DistutilsOptionError("You need to specify the output "
                                          "directory for the generated files")
           if self.i18n_module is None:
               raise DistutilsOptionError("You need to specify from which module "
                                          "the '_()' function should be imported "
                                          "from. Example: mymodule.i18n")

       def run(self):
           for filename in os.listdir(self.input_dir):
               fpath = os.path.join(self.input_dir, filename)
               if not os.path.isfile(fpath):
                   continue
               elif not filename.endswith('.ui'):
                   continue
               self.compile_ui(fpath)


       def compile_ui(self, ui_file, py_file=None):
           """Compile the .ui files to python modules."""
           self._wrapuic(i18n_module=self.i18n_module)
           if py_file is None:
               py_file = os.path.join(
                   self.output_dir,
                   os.path.basename(ui_file).replace('.ui', '_ui.py')
               )

           fi = open(ui_file, 'r')
           fo = open(py_file, 'wt')
           try:
               from pysideuic import compileUi
               compileUi(fi, fo, execute=self.ui_execute, indent=self.indent,
                         from_imports=self.from_imports)
               log.info("Compiled %s into %s", ui_file, py_file)
           except ImportError:
               log.warn("You need to have pyside-tools installed in order to "
                        "compile .ui files.")
           except Exception, err:
               log.warn("Failed to generate %r from %r: %s", py_file, ui_file, err)
               if not os.path.exists(py_file) or not not file(py_file).read():
                   raise SystemExit(1)
               return
           finally:
               fi.close()
               fo.close()

       _wrappeduic = False
       @classmethod
       def _wrapuic(cls, i18n_module=None):
           """Wrap uic to use gettext's _() in place of tr()"""
           if cls._wrappeduic:
               return

           try:
               from pysideuic.Compiler import compiler, qtproxies, indenter

               class _UICompiler(compiler.UICompiler):
                   """Specialised compiler for qt .ui files."""
                   def createToplevelWidget(self, classname, widgetname):
                       o = indenter.getIndenter()
                       o.level = 0
                       o.write('from %s import _' % i18n_module)
                       return super(_UICompiler, self).createToplevelWidget(
                           classname, widgetname
                       )
               compiler.UICompiler = _UICompiler

               class _i18n_string(qtproxies.i18n_string):
                   """Provide a translated text."""
                   def __str__(self):
                       return "_('%s')" % self.string.encode('string-escape')

               qtproxies.i18n_string = _i18n_string

               cls._wrappeduic = True
           except ImportError:
               log.warn("You need to have pyside-tools installed in order to "
                        "compile .ui files.")


And there you have it!

.. _`PySide`: http://www.pyside.org/
