create table if not exists tasks (
    id integer primary key autoincrement,
    deleted_at integer,
    created_at integer not null,
    updated_at integer,
    title varchar not null,
    todo_id integer,
    expired_at integer not null,
    foreign key (todo_id) references todolist (id)
);

create trigger if not exists update_updated_at_current_timestamp
    after update on tasks
    for each row
    when new.updated_at <= old.updated_at or new.updated_at is null
    begin
        update tasks set updated_at=current_timestamp where id = new.id;
    end;