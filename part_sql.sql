USE bot_manager; -- Выбираем базу для дальнейших операций


-- Создаем таблицу родителя
CREATE TABLE parent ( 
    id INT NOT NULL,
    name VARCHAR(30),
    PRIMARY KEY (id)
);

-- создаем таблицу потомка который имеет связь с таблицей родителя
CREATE TABLE child(
    id INT,
    parent_id INT,
    FOREIGN KEY (parent_id)
        REFERENCES parent(id)
        ON DELETE CASCADE
);

-- Добавляем какие то данные в обе таблицы, в таблицу потомка указываем на ID к записи родителя которому будет относится запись в потомке
INSERT INTO parent (id, name)
VALUES (1, 'Вася');

INSERT INTO child (id, parent_id)
VALUES (1, 1);

-- Теперь для получение данных можно использовать JOIN, в данном случае будет объеденены таблицы parent и child которые связанны друг с другом
SELECT parent.*, child.*
FROM parent
INNER JOIN child ON child.parent_id = parent.id
