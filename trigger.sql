---------------------------- Delete Trigger ------------------------------------

create or replace function delete_id_trigger() 
RETURNS trigger AS $$
begin perform pg_notify('del_id'::text, old::text); 
return new; 
end; 
$$ language plpgsql;


create trigger triggerDelete 
after delete on public."FileInfos" 
for each row 
execute procedure delete_id_trigger();

--------------------------- Delete Command -------------------------------------
DELETE FROM public."FileInfos" WHERE "FileName" = 'TestFile'

------------------------------------- Create Trigger ---------------------------
create or replace function create_id_trigger() 
RETURNS trigger AS $$
begin perform pg_notify('new_id'::text, new::text); 
return new; 
end; 
$$ language plpgsql;


create trigger triggerCreate 
after insert on public."FileInfos" 
for each row 
execute procedure create_id_trigger();

------------------------------------- Update Trigger ---------------------------

create or replace function update_id_trigger() 
RETURNS trigger AS $$
begin perform pg_notify('update_id'::text, new::text); 
return new; 
end; 
$$ language plpgsql;


create trigger triggerUpdate
after update on public."FileInfos" 
for each row 
execute procedure update_id_trigger();

---------------------------------------------------------------------------------
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
