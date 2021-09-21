create trigger trigger1 
after insert or update on public."FileInfos" 
for each row 
execute procedure notify_id_trigger();


create or replace function notify_id_trigger() 
RETURNS trigger AS $$
begin perform pg_notify('new_id'::text, new::text); 
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
