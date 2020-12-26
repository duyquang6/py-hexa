create table if not exists todolist (
    id integer primary key autoincrement,
    deleted_at integer,
    created_at integer not null,
    updated_at integer,
    author text not null
);

create trigger if not exists update_updated_at_current_timestamp
    after update on todolist
    for each row
    when new.updated_at <= old.updated_at or new.updated_at is null
    begin
        update todolist set updated_at=current_timestamp where id = new.id;
    end;