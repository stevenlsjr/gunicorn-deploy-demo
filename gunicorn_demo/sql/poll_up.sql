
CREATE TABLE IF NOT EXISTS poll (
  id                SERIAL PRIMARY KEY,
  name              VARCHAR UNIQUE,
  description       VARCHAR NULL,
  agree_count       INT DEFAULT(0),
  disagree_count    INT DEFAULT(0),
  created           TIMESTAMP WITH TIME ZONE DEFAULT(now())
);

INSERT INTO poll
  (name, agree_count, disagree_count) 
VALUES
  ('Is water wet?', 10, 200),
  ('What is your favorite color?', 2, 0)
ON CONFLICT DO NOTHING;