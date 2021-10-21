---------------------------- Delete Trigger ------------------------------------

create trigger trigger2 
after DELETE on public."FileInfos" 
for each row 
execute procedure notify_del_trigger();

create or replace function notify_del_trigger() 
RETURNS trigger AS $$
begin perform pg_notify('del_id'::text, old::text); 
return new; 
end; 
$$ language plpgsql;

--------------------------- Delete Command -------------------------------------
DELETE FROM public."FileInfos" WHERE "FileName" = 'TestFile'

------------------------------------- Create Trigger ---------------------------
create trigger trigger1 
after insert or update on public."FileInfos" 
for each row 
execute procedure notify_id_trigger();


create or replace function notify_id_trigger() 
RETURNS trigger AS $$
begin perform pg_notify('new_id'::text, new::text);  -- wichtig !!
return new; 
end; 
$$ language plpgsql;


create or replace function notify_id_trigger() 
RETURNS trigger AS $$
begin 
perform pg_notify('new_id'::text, new."LastModifiedDateTime"::text || new."FileName"::text); 
return new; 
end; 
$$ language plpgsql;

create or replace function notify_id_trigger() 
RETURNS trigger AS $$
begin perform pg_notify('new_id'::text, new."Id"::text); 
return new; 
end; 
$$ language plpgsql;


create or replace function notify_id_trigger() 
RETURNS trigger AS $$
begin perform pg_notify('new_id'::text, new."LastModifiedDateTime"::text); 
return new; 
end; 
$$ language plpgsql;
