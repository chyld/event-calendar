DROP TABLE IF EXISTS events
;

CREATE TABLE
  events (
    id INTEGER NOT NULL PRIMARY KEY, -- 64 bit (+/- 9 quintillion)
    title TEXT
  , start TEXT
  , stop TEXT
  , color TEXT
  , graphic TEXT
  )
;

DROP TABLE IF EXISTS notes
;

CREATE TABLE
  notes (
    id INTEGER NOT NULL PRIMARY KEY, -- 64 bit (+/- 9 quintillion)
    note TEXT
  , cal TEXT
  , color TEXT
  , graphic TEXT
  )
;
