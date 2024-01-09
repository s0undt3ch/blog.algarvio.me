Postgres Cron Backups
#####################
:date: 2011-07-03 08:40
:author: s0undt3ch
:slug: postgres-cron-backups
:url: 2011/07/03/postgres-cron-backups
:save_as: 2011/07/03/postgres-cron-backups/index.html
:category: Linux
:tags: Postgres Bash Backup
:summary: So, I found myself with the need to make automatic backups of my postgres databases...

          After some `Google <http://www.google.com>`_'ing and reading of some peoples recipes, here's mine.


So, I found myself with the need to make automatic backups of my postgres databases...

After some `Google <http://www.google.com>`_'ing and reading of some peoples recipes, here's mine.

.. code-block:: sh

   #!/bin/bash
   PG_USER="postgres"
   SUDO_CMD=$(which sudo)
   SUDO="$SUDO_CMD -u $PG_USER"
   PSQL_CMD=$(which psql)
   PSQL="$SUDO $PSQL_CMD"
   GREP=$(which grep)
   AWK=$(which awk)
   PGDUMP_CMD=$(which pg_dump)
   PGDUMP="$SUDO $PGDUMP_CMD"
   VACUUM_CMD=$(which vacuumdb)
   VACUUM="$SUDO $VACUUM_CMD"
   FIND=$(which find)

   # Bellow is how old, in days, a backup will need to be deleted.
   # This helps cleaning up and don't keep piling backups
   MAX_DAYS=3

   # Backups destination directory
   BACKUPS_DIR="/var/backups/postgresql"

   # To get a list of all databases uncomment the following 3 lines
   #DBS=$($PSQL -q -c "\l" | sed -n 4,/\eof/p | grep -v rows\) | grep -v template0 | grep -v template1 | awk {'print $1'} | grep -v :)
   #echo $DBS
   #exit

   # Uncomment bellow to backup all databases
   #DBS=$($PSQL -q -c "\l" | sed -n 4,/\eof/p | grep -v rows\) | grep -v template0 | grep -v template1 | awk {'print $1'} | grep -v :)

   # Uncomment bellow and add the database names you wish to back separated with a white-space
   #DBS=""
   
   for DB in $DBS
       do
           echo -n "Vacuum'ing database $DB ... "
           $($VACUUM $DB)
           echo "Done."
           BACKUP_NAME="$BACKUPS_DIR/$DB-backup-$(date +%Y-%m-%d).sql.tar"
           echo -n "Creating backup of database $DB ... "
           $($PGDUMP -o -F t $DB > $BACKUP_NAME)
           echo "Done."
           echo -n "Removing backups of database $DB older than $MAX_DAYS days ... "
           $($FIND $BACKUPS_DIR -name "$DB*" -type f -mtime +3 -delete)
           echo "Done."
           echo "----8<----8<----8<----8<----8<----8<----8<----8<----8<----8<----8<----8<----8<----"
     done
