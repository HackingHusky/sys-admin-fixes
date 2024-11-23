USE MASTER
declare
   @isql varchar(2000),
   @dbname varchar(64)
   
   declare c1 cursor for select name from master..sysdatabases where name not in ('master','model','msdb','tempdb')
   open c1
   fetch next from c1 into @dbname
   While @@fetch_status <> -1
      begin
      select @isql = 'ALTER DATABASE @dbname SET AUTO_CLOSE OFF'
      select @isql = replace(@isql,'@dbname',@dbname)
      print @isql
      exec(@isql)

	  fetch next from c1 into @dbname
      end
 close c1
 deallocate c1
