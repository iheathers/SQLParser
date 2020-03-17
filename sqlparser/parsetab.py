
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ALTER AND AS ASC AVG BETWEEN BIGINT BY CHAR COLUMN COMMA COMPARISON COUNT CREATE DECIMAL DELETE DESC DISTINCT DOUBLE DROP END FLOAT FROM FULL GROUP HAVING IN INNER INSERT INT INTEGER INTO IS JOIN LEFT LIKE LIMIT MAX MEDIUMINT MIN NOT NULL NUMBER ON OR ORDER QSTRING RIGHT SELECT SET SHOW SMALLINT STRING SUM TABLE TINYINT UPDATE VALUES VARCHAR WHERE expression : dml END\n                   | ddl END\n     dml : select\n            | update\n            | insert\n            | delete\n     ddl : create\n            | alter\n            | drop\n     select : SELECT columns FROM table join where group_by having order_by limit\n     table : table COMMA table\n              | STRING AS STRING\n              | STRING STRING\n              | STRING\n     join : INNER JOIN table on join\n             | LEFT JOIN table on join\n             | RIGHT JOIN table on join\n             | FULL JOIN table on join\n             | JOIN table on join\n             | empty\n     on : ON item COMPARISON item\n     where : WHERE conditions\n              | empty\n     group_by : GROUP BY strings\n                 | empty\n     having : HAVING conditions\n               | empty\n     order_by : ORDER BY order\n                 | empty\n     limit : LIMIT numbers\n              | empty\n     order : order COMMA order\n              | string order_type\n     order_type : ASC\n                   | DESC\n                   | empty\n     update : UPDATE table SET set where\n     set : set COMMA set\n            | item COMPARISON item\n     insert : INSERT into table insert_columns VALUES values\n     into : INTO\n             | empty\n     insert_columns : "(" columns ")"\n                       | empty\n     value : value COMMA value\n              | string\n              | NUMBER\n     values : values COMMA values\n               | "(" value ")"\n     delete : DELETE FROM table where\n     create : CREATE TABLE string "(" create_columns ")"\n     create_columns : create_columns COMMA create_columns\n                       | string datatype\n     datatype : INT\n                 | INTEGER\n                 | TINYINT\n                 | SMALLINT\n                 | MEDIUMINT\n                 | BIGINT\n                 | FLOAT\n                 | DOUBLE\n                 | DECIMAL\n                 | CHAR "(" NUMBER ")"\n                 | VARCHAR "(" NUMBER ")"\n     alter : ALTER TABLE string change_column\n     change_column : ADD string datatype\n                      | DROP COLUMN string\n                      | ALTER COLUMN string datatype\n     drop : DROP TABLE string\n     columns : columns COMMA columns\n                | column_as\n                | column\n     column_as : column AS item\n                  | column item\n     column : function "(" distinct_item ")"\n               | function "(" item ")"\n               | distinct_item\n               | item\n     distinct_item : DISTINCT item\n                      | DISTINCT "(" item ")"\n     function : COUNT\n                 | SUM\n                 | AVG\n                 | MIN\n                 | MAX\n     item : string\n             | NUMBER\n             | "*"\n             | string "." item\n     numbers : numbers COMMA numbers\n                | NUMBER\n     strings : strings COMMA strings\n                | string\n     items : strings\n              | numbers\n     string : STRING\n               | QSTRING\n     conditions : conditions AND conditions\n                   | conditions OR conditions\n                   | "(" conditions ")"\n                   | compare\n     compare : column COMPARISON item\n                | column like QSTRING\n                | column BETWEEN item AND item\n                | column IS null\n                | column in lritems\n     lritems : "(" items ")"\n     like : LIKE\n             | NOT LIKE\n     in : IN\n           | NOT IN\n     null : NULL\n             | NOT NULL\n    empty :'
    
_lr_action_items = {'SELECT':([0,],[11,]),'UPDATE':([0,],[12,]),'INSERT':([0,],[13,]),'DELETE':([0,],[14,]),'CREATE':([0,],[15,]),'ALTER':([0,35,36,61,],[16,-96,-97,81,]),'DROP':([0,35,36,61,],[17,-96,-97,84,]),'$end':([1,18,19,],[0,-1,-2,]),'END':([2,3,4,5,6,7,8,9,10,32,33,34,35,36,38,56,59,62,63,69,70,72,73,77,79,82,85,91,95,100,102,109,115,116,117,132,133,134,135,136,137,138,139,140,143,146,147,148,150,152,161,162,163,164,165,167,168,170,177,178,180,182,183,185,186,187,188,189,192,196,197,200,202,203,204,205,207,208,209,211,212,215,216,217,219,221,222,223,224,225,226,228,229,230,231,232,],[18,19,-3,-4,-5,-6,-7,-8,-9,-86,-87,-88,-96,-97,-14,-13,-114,-69,-114,-89,-114,-11,-12,-50,-23,-65,-114,-20,-37,-22,-101,-114,-38,-39,-40,-54,-55,-56,-57,-58,-59,-60,-61,-62,-51,-66,-67,-114,-25,-114,-98,-99,-100,-102,-103,-105,-112,-106,-68,-114,-27,-114,-19,-114,-114,-114,-48,-49,-113,-93,-91,-114,-29,-26,-24,-15,-16,-17,-18,-104,-107,-63,-64,-10,-31,-21,-92,-90,-30,-28,-114,-33,-34,-35,-36,-32,]),'COUNT':([11,47,75,78,101,120,121,179,],[26,26,26,26,26,26,26,26,]),'SUM':([11,47,75,78,101,120,121,179,],[27,27,27,27,27,27,27,27,]),'AVG':([11,47,75,78,101,120,121,179,],[28,28,28,28,28,28,28,28,]),'MIN':([11,47,75,78,101,120,121,179,],[29,29,29,29,29,29,29,29,]),'MAX':([11,47,75,78,101,120,121,179,],[30,30,30,30,30,30,30,30,]),'DISTINCT':([11,47,50,75,78,101,120,121,179,],[31,31,31,31,31,31,31,31,31,]),'NUMBER':([11,22,23,25,31,32,33,34,35,36,47,48,50,51,52,53,54,69,75,78,92,93,94,96,97,101,118,120,121,123,125,153,171,174,175,179,190,191,206,214,218,],[33,33,-78,-77,33,-86,-87,-88,-96,-97,33,33,33,-79,33,33,33,-89,33,33,-75,-76,-80,33,33,33,160,33,33,33,33,33,197,198,199,33,160,33,33,197,197,]),'*':([11,22,23,25,31,32,33,34,35,36,47,48,50,51,52,53,54,69,75,78,92,93,94,96,97,101,120,121,123,125,153,179,191,206,],[34,34,-78,-77,34,-86,-87,-88,-96,-97,34,34,34,-79,34,34,34,-89,34,34,-75,-76,-80,34,34,34,34,34,34,34,34,34,34,34,]),'STRING':([11,12,13,22,23,25,31,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,55,57,69,75,78,80,83,87,92,93,94,96,97,101,106,108,110,112,113,114,118,120,121,123,125,144,153,171,179,181,190,191,206,213,220,227,],[35,38,-114,35,-78,-77,35,-86,-87,-88,-96,-97,56,38,-41,-42,38,35,35,35,38,35,35,35,-79,35,35,35,38,73,-89,35,35,35,35,38,-75,-76,-80,35,35,35,35,35,38,38,38,38,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'QSTRING':([11,22,23,25,31,32,33,34,35,36,43,44,45,47,48,50,51,52,53,54,69,75,78,80,83,92,93,94,96,97,101,106,108,118,120,121,123,124,125,128,144,153,171,172,179,181,190,191,206,213,220,227,],[36,36,-78,-77,36,-86,-87,-88,-96,-97,36,36,36,36,36,36,-79,36,36,36,-89,36,36,36,36,-75,-76,-80,36,36,36,36,36,36,36,36,36,165,36,-108,36,36,36,-109,36,36,36,36,36,36,36,36,]),'INTO':([13,],[40,]),'FROM':([14,20,21,22,23,25,32,33,34,35,36,49,51,64,65,69,92,93,94,],[42,46,-71,-72,-78,-77,-86,-87,-88,-96,-97,-74,-79,-70,-73,-89,-75,-76,-80,]),'TABLE':([15,16,17,],[43,44,45,]),'COMMA':([20,21,22,23,25,32,33,34,35,36,37,38,49,51,56,58,59,63,64,65,69,70,72,73,92,93,94,99,105,111,115,116,117,131,132,133,134,135,136,137,138,139,140,151,154,155,156,158,159,160,176,188,189,194,195,196,197,204,210,215,216,222,223,224,225,226,228,229,230,231,232,],[47,-71,-72,-78,-77,-86,-87,-88,-96,-97,55,-14,-74,-79,-13,55,55,55,47,-73,-89,96,55,-12,-75,-76,-80,47,144,55,96,-39,157,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,55,55,55,55,190,-46,-47,144,157,-49,213,214,-93,-91,213,190,-63,-64,213,214,214,227,-114,-33,-34,-35,-36,227,]),')':([21,22,23,25,32,33,34,35,36,49,51,64,65,66,67,68,69,92,93,94,99,102,105,122,131,132,133,134,135,136,137,138,139,140,158,159,160,161,162,163,164,165,167,168,170,176,192,193,194,195,196,197,198,199,210,211,212,215,216,222,223,],[-71,-72,-78,-77,-86,-87,-88,-96,-97,-74,-79,-70,-73,92,93,94,-89,-75,-76,-80,119,-101,143,163,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,189,-46,-47,-98,-99,-100,-102,-103,-105,-112,-106,-52,-113,212,-94,-95,-93,-91,215,216,-45,-104,-107,-63,-64,-92,-90,]),'AS':([22,23,25,32,33,34,35,36,38,51,69,92,93,94,],[48,-78,-77,-86,-87,-88,-96,-97,57,-79,-89,-75,-76,-80,]),'COMPARISON':([23,25,32,33,34,35,36,51,69,71,92,93,94,103,184,],[-78,-77,-86,-87,-88,-96,-97,-79,-89,97,-75,-76,-80,123,206,]),'BETWEEN':([23,25,32,33,34,35,36,51,69,92,93,94,103,],[-78,-77,-86,-87,-88,-96,-97,-79,-89,-75,-76,-80,125,]),'IS':([23,25,32,33,34,35,36,51,69,92,93,94,103,],[-78,-77,-86,-87,-88,-96,-97,-79,-89,-75,-76,-80,126,]),'LIKE':([23,25,32,33,34,35,36,51,69,92,93,94,103,129,],[-78,-77,-86,-87,-88,-96,-97,-79,-89,-75,-76,-80,128,172,]),'NOT':([23,25,32,33,34,35,36,51,69,92,93,94,103,126,],[-78,-77,-86,-87,-88,-96,-97,-79,-89,-75,-76,-80,129,169,]),'IN':([23,25,32,33,34,35,36,51,69,92,93,94,103,129,],[-78,-77,-86,-87,-88,-96,-97,-79,-89,-75,-76,-80,130,173,]),'(':([24,26,27,28,29,30,31,35,36,38,56,58,60,72,73,78,98,101,120,121,127,130,141,142,157,173,179,],[50,-81,-82,-83,-84,-85,52,-96,-97,-14,-13,75,80,-11,-12,101,118,101,101,101,171,-110,174,175,118,-111,101,]),'WHERE':([32,33,34,35,36,38,56,59,63,69,70,72,73,85,91,115,116,152,182,183,185,186,187,205,207,208,209,221,],[-86,-87,-88,-96,-97,-14,-13,78,-114,-89,78,-11,-12,78,-20,-38,-39,-114,-114,-19,-114,-114,-114,-15,-16,-17,-18,-21,]),'AND':([32,33,34,35,36,69,100,102,122,161,162,163,164,165,166,167,168,170,192,203,211,212,],[-86,-87,-88,-96,-97,-89,120,-101,120,120,120,-100,-102,-103,191,-105,-112,-106,-113,120,-104,-107,]),'OR':([32,33,34,35,36,69,100,102,122,161,162,163,164,165,167,168,170,192,203,211,212,],[-86,-87,-88,-96,-97,-89,121,-101,121,121,121,-100,-102,-103,-105,-112,-106,-113,121,-104,-107,]),'GROUP':([32,33,34,35,36,38,56,63,69,72,73,79,85,91,100,102,109,152,161,162,163,164,165,167,168,170,182,183,185,186,187,192,205,207,208,209,211,212,221,],[-86,-87,-88,-96,-97,-14,-13,-114,-89,-11,-12,-23,-114,-20,-22,-101,149,-114,-98,-99,-100,-102,-103,-105,-112,-106,-114,-19,-114,-114,-114,-113,-15,-16,-17,-18,-104,-107,-21,]),'HAVING':([32,33,34,35,36,38,56,63,69,72,73,79,85,91,100,102,109,148,150,152,161,162,163,164,165,167,168,170,182,183,185,186,187,192,196,204,205,207,208,209,211,212,221,222,],[-86,-87,-88,-96,-97,-14,-13,-114,-89,-11,-12,-23,-114,-20,-22,-101,-114,179,-25,-114,-98,-99,-100,-102,-103,-105,-112,-106,-114,-19,-114,-114,-114,-113,-93,-24,-15,-16,-17,-18,-104,-107,-21,-92,]),'ORDER':([32,33,34,35,36,38,56,63,69,72,73,79,85,91,100,102,109,148,150,152,161,162,163,164,165,167,168,170,178,180,182,183,185,186,187,192,196,203,204,205,207,208,209,211,212,221,222,],[-86,-87,-88,-96,-97,-14,-13,-114,-89,-11,-12,-23,-114,-20,-22,-101,-114,-114,-25,-114,-98,-99,-100,-102,-103,-105,-112,-106,201,-27,-114,-19,-114,-114,-114,-113,-93,-26,-24,-15,-16,-17,-18,-104,-107,-21,-92,]),'LIMIT':([32,33,34,35,36,38,56,63,69,72,73,79,85,91,100,102,109,148,150,152,161,162,163,164,165,167,168,170,178,180,182,183,185,186,187,192,196,200,202,203,204,205,207,208,209,211,212,221,222,225,226,228,229,230,231,232,],[-86,-87,-88,-96,-97,-14,-13,-114,-89,-11,-12,-23,-114,-20,-22,-101,-114,-114,-25,-114,-98,-99,-100,-102,-103,-105,-112,-106,-114,-27,-114,-19,-114,-114,-114,-113,-93,218,-29,-26,-24,-15,-16,-17,-18,-104,-107,-21,-92,-28,-114,-33,-34,-35,-36,-32,]),'INNER':([32,33,34,35,36,38,56,63,69,72,73,152,182,185,186,187,221,],[-86,-87,-88,-96,-97,-14,-13,86,-89,-11,-12,86,86,86,86,86,-21,]),'LEFT':([32,33,34,35,36,38,56,63,69,72,73,152,182,185,186,187,221,],[-86,-87,-88,-96,-97,-14,-13,88,-89,-11,-12,88,88,88,88,88,-21,]),'RIGHT':([32,33,34,35,36,38,56,63,69,72,73,152,182,185,186,187,221,],[-86,-87,-88,-96,-97,-14,-13,89,-89,-11,-12,89,89,89,89,89,-21,]),'FULL':([32,33,34,35,36,38,56,63,69,72,73,152,182,185,186,187,221,],[-86,-87,-88,-96,-97,-14,-13,90,-89,-11,-12,90,90,90,90,90,-21,]),'JOIN':([32,33,34,35,36,38,56,63,69,72,73,86,88,89,90,152,182,185,186,187,221,],[-86,-87,-88,-96,-97,-14,-13,87,-89,-11,-12,110,112,113,114,87,87,87,87,87,-21,]),'.':([32,35,36,],[53,-96,-97,]),'ADD':([35,36,61,],[-96,-97,83,]),'INT':([35,36,104,107,145,],[-96,-97,132,132,132,]),'INTEGER':([35,36,104,107,145,],[-96,-97,133,133,133,]),'TINYINT':([35,36,104,107,145,],[-96,-97,134,134,134,]),'SMALLINT':([35,36,104,107,145,],[-96,-97,135,135,135,]),'MEDIUMINT':([35,36,104,107,145,],[-96,-97,136,136,136,]),'BIGINT':([35,36,104,107,145,],[-96,-97,137,137,137,]),'FLOAT':([35,36,104,107,145,],[-96,-97,138,138,138,]),'DOUBLE':([35,36,104,107,145,],[-96,-97,139,139,139,]),'DECIMAL':([35,36,104,107,145,],[-96,-97,140,140,140,]),'CHAR':([35,36,104,107,145,],[-96,-97,141,141,141,]),'VARCHAR':([35,36,104,107,145,],[-96,-97,142,142,142,]),'ASC':([35,36,226,],[-96,-97,229,]),'DESC':([35,36,226,],[-96,-97,230,]),'SET':([37,38,56,72,73,],[54,-14,-13,-11,-12,]),'VALUES':([38,56,58,72,73,74,76,119,],[-14,-13,-114,-11,-12,98,-44,-43,]),'ON':([38,56,72,73,111,151,154,155,156,],[-14,-13,-11,-12,153,153,153,153,153,]),'COLUMN':([81,84,],[106,108,]),'NULL':([126,169,],[168,192,]),'BY':([149,201,],[181,220,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'dml':([0,],[2,]),'ddl':([0,],[3,]),'select':([0,],[4,]),'update':([0,],[5,]),'insert':([0,],[6,]),'delete':([0,],[7,]),'create':([0,],[8,]),'alter':([0,],[9,]),'drop':([0,],[10,]),'columns':([11,47,75,],[20,64,99,]),'column_as':([11,47,75,],[21,21,21,]),'column':([11,47,75,78,101,120,121,179,],[22,22,22,103,103,103,103,103,]),'item':([11,22,31,47,48,50,52,53,54,75,78,96,97,101,120,121,123,125,153,179,191,206,],[23,49,51,23,65,67,68,69,71,23,23,71,116,23,23,23,164,166,184,23,211,221,]),'function':([11,47,75,78,101,120,121,179,],[24,24,24,24,24,24,24,24,]),'distinct_item':([11,47,50,75,78,101,120,121,179,],[25,25,66,25,25,25,25,25,25,]),'string':([11,22,31,43,44,45,47,48,50,52,53,54,75,78,80,83,96,97,101,106,108,118,120,121,123,125,144,153,171,179,181,190,191,206,213,220,227,],[32,32,32,60,61,62,32,32,32,32,32,32,32,32,104,107,32,32,32,145,147,159,32,32,32,32,104,32,196,32,196,159,32,32,196,226,226,]),'table':([12,39,42,46,55,87,110,112,113,114,],[37,58,59,63,72,111,151,154,155,156,]),'into':([13,],[39,]),'empty':([13,58,59,63,70,85,109,148,152,178,182,185,186,187,200,226,],[41,76,79,91,79,79,150,180,91,202,91,91,91,91,219,231,]),'set':([54,96,],[70,115,]),'insert_columns':([58,],[74,]),'where':([59,70,85,],[77,95,109,]),'change_column':([61,],[82,]),'join':([63,152,182,185,186,187,],[85,183,205,207,208,209,]),'conditions':([78,101,120,121,179,],[100,122,161,162,203,]),'compare':([78,101,120,121,179,],[102,102,102,102,102,]),'create_columns':([80,144,],[105,176,]),'values':([98,157,],[117,188,]),'like':([103,],[124,]),'in':([103,],[127,]),'datatype':([104,107,145,],[131,146,177,]),'group_by':([109,],[148,]),'on':([111,151,154,155,156,],[152,182,185,186,187,]),'value':([118,190,],[158,210,]),'null':([126,],[167,]),'lritems':([127,],[170,]),'having':([148,],[178,]),'items':([171,],[193,]),'strings':([171,181,213,],[194,204,222,]),'numbers':([171,214,218,],[195,223,224,]),'order_by':([178,],[200,]),'limit':([200,],[217,]),'order':([220,227,],[225,232,]),'order_type':([226,],[228,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> dml END','expression',2,'p_expression','grammar.py',10),
  ('expression -> ddl END','expression',2,'p_expression','grammar.py',11),
  ('dml -> select','dml',1,'p_dml','grammar.py',16),
  ('dml -> update','dml',1,'p_dml','grammar.py',17),
  ('dml -> insert','dml',1,'p_dml','grammar.py',18),
  ('dml -> delete','dml',1,'p_dml','grammar.py',19),
  ('ddl -> create','ddl',1,'p_ddl','grammar.py',25),
  ('ddl -> alter','ddl',1,'p_ddl','grammar.py',26),
  ('ddl -> drop','ddl',1,'p_ddl','grammar.py',27),
  ('select -> SELECT columns FROM table join where group_by having order_by limit','select',10,'p_select','grammar.py',36),
  ('table -> table COMMA table','table',3,'p_table','grammar.py',51),
  ('table -> STRING AS STRING','table',3,'p_table','grammar.py',52),
  ('table -> STRING STRING','table',2,'p_table','grammar.py',53),
  ('table -> STRING','table',1,'p_table','grammar.py',54),
  ('join -> INNER JOIN table on join','join',5,'p_join','grammar.py',68),
  ('join -> LEFT JOIN table on join','join',5,'p_join','grammar.py',69),
  ('join -> RIGHT JOIN table on join','join',5,'p_join','grammar.py',70),
  ('join -> FULL JOIN table on join','join',5,'p_join','grammar.py',71),
  ('join -> JOIN table on join','join',4,'p_join','grammar.py',72),
  ('join -> empty','join',1,'p_join','grammar.py',73),
  ('on -> ON item COMPARISON item','on',4,'p_on','grammar.py',82),
  ('where -> WHERE conditions','where',2,'p_where','grammar.py',87),
  ('where -> empty','where',1,'p_where','grammar.py',88),
  ('group_by -> GROUP BY strings','group_by',3,'p_group_by','grammar.py',95),
  ('group_by -> empty','group_by',1,'p_group_by','grammar.py',96),
  ('having -> HAVING conditions','having',2,'p_having','grammar.py',103),
  ('having -> empty','having',1,'p_having','grammar.py',104),
  ('order_by -> ORDER BY order','order_by',3,'p_order_by','grammar.py',111),
  ('order_by -> empty','order_by',1,'p_order_by','grammar.py',112),
  ('limit -> LIMIT numbers','limit',2,'p_limit','grammar.py',120),
  ('limit -> empty','limit',1,'p_limit','grammar.py',121),
  ('order -> order COMMA order','order',3,'p_order','grammar.py',130),
  ('order -> string order_type','order',2,'p_order','grammar.py',131),
  ('order_type -> ASC','order_type',1,'p_order_type','grammar.py',139),
  ('order_type -> DESC','order_type',1,'p_order_type','grammar.py',140),
  ('order_type -> empty','order_type',1,'p_order_type','grammar.py',141),
  ('update -> UPDATE table SET set where','update',5,'p_update','grammar.py',153),
  ('set -> set COMMA set','set',3,'p_set','grammar.py',163),
  ('set -> item COMPARISON item','set',3,'p_set','grammar.py',164),
  ('insert -> INSERT into table insert_columns VALUES values','insert',6,'p_insert','grammar.py',175),
  ('into -> INTO','into',1,'p_into','grammar.py',185),
  ('into -> empty','into',1,'p_into','grammar.py',186),
  ('insert_columns -> ( columns )','insert_columns',3,'p_insert_columns','grammar.py',191),
  ('insert_columns -> empty','insert_columns',1,'p_insert_columns','grammar.py',192),
  ('value -> value COMMA value','value',3,'p_value','grammar.py',199),
  ('value -> string','value',1,'p_value','grammar.py',200),
  ('value -> NUMBER','value',1,'p_value','grammar.py',201),
  ('values -> values COMMA values','values',3,'p_values','grammar.py',209),
  ('values -> ( value )','values',3,'p_values','grammar.py',210),
  ('delete -> DELETE FROM table where','delete',4,'p_delete','grammar.py',221),
  ('create -> CREATE TABLE string ( create_columns )','create',6,'p_create','grammar.py',233),
  ('create_columns -> create_columns COMMA create_columns','create_columns',3,'p_create_columns','grammar.py',243),
  ('create_columns -> string datatype','create_columns',2,'p_create_columns','grammar.py',244),
  ('datatype -> INT','datatype',1,'p_datatype','grammar.py',252),
  ('datatype -> INTEGER','datatype',1,'p_datatype','grammar.py',253),
  ('datatype -> TINYINT','datatype',1,'p_datatype','grammar.py',254),
  ('datatype -> SMALLINT','datatype',1,'p_datatype','grammar.py',255),
  ('datatype -> MEDIUMINT','datatype',1,'p_datatype','grammar.py',256),
  ('datatype -> BIGINT','datatype',1,'p_datatype','grammar.py',257),
  ('datatype -> FLOAT','datatype',1,'p_datatype','grammar.py',258),
  ('datatype -> DOUBLE','datatype',1,'p_datatype','grammar.py',259),
  ('datatype -> DECIMAL','datatype',1,'p_datatype','grammar.py',260),
  ('datatype -> CHAR ( NUMBER )','datatype',4,'p_datatype','grammar.py',261),
  ('datatype -> VARCHAR ( NUMBER )','datatype',4,'p_datatype','grammar.py',262),
  ('alter -> ALTER TABLE string change_column','alter',4,'p_alter','grammar.py',273),
  ('change_column -> ADD string datatype','change_column',3,'p_change_column','grammar.py',282),
  ('change_column -> DROP COLUMN string','change_column',3,'p_change_column','grammar.py',283),
  ('change_column -> ALTER COLUMN string datatype','change_column',4,'p_change_column','grammar.py',284),
  ('drop -> DROP TABLE string','drop',3,'p_drop','grammar.py',297),
  ('columns -> columns COMMA columns','columns',3,'p_columns','grammar.py',309),
  ('columns -> column_as','columns',1,'p_columns','grammar.py',310),
  ('columns -> column','columns',1,'p_columns','grammar.py',311),
  ('column_as -> column AS item','column_as',3,'p_column_as','grammar.py',320),
  ('column_as -> column item','column_as',2,'p_column_as','grammar.py',321),
  ('column -> function ( distinct_item )','column',4,'p_column','grammar.py',330),
  ('column -> function ( item )','column',4,'p_column','grammar.py',331),
  ('column -> distinct_item','column',1,'p_column','grammar.py',332),
  ('column -> item','column',1,'p_column','grammar.py',333),
  ('distinct_item -> DISTINCT item','distinct_item',2,'p_distinct_item','grammar.py',341),
  ('distinct_item -> DISTINCT ( item )','distinct_item',4,'p_distinct_item','grammar.py',342),
  ('function -> COUNT','function',1,'p_function','grammar.py',350),
  ('function -> SUM','function',1,'p_function','grammar.py',351),
  ('function -> AVG','function',1,'p_function','grammar.py',352),
  ('function -> MIN','function',1,'p_function','grammar.py',353),
  ('function -> MAX','function',1,'p_function','grammar.py',354),
  ('item -> string','item',1,'p_item','grammar.py',359),
  ('item -> NUMBER','item',1,'p_item','grammar.py',360),
  ('item -> *','item',1,'p_item','grammar.py',361),
  ('item -> string . item','item',3,'p_item','grammar.py',362),
  ('numbers -> numbers COMMA numbers','numbers',3,'p_numbers','grammar.py',372),
  ('numbers -> NUMBER','numbers',1,'p_numbers','grammar.py',373),
  ('strings -> strings COMMA strings','strings',3,'p_strings','grammar.py',381),
  ('strings -> string','strings',1,'p_strings','grammar.py',382),
  ('items -> strings','items',1,'p_items','grammar.py',390),
  ('items -> numbers','items',1,'p_items','grammar.py',391),
  ('string -> STRING','string',1,'p_string','grammar.py',397),
  ('string -> QSTRING','string',1,'p_string','grammar.py',398),
  ('conditions -> conditions AND conditions','conditions',3,'p_conditions','grammar.py',404),
  ('conditions -> conditions OR conditions','conditions',3,'p_conditions','grammar.py',405),
  ('conditions -> ( conditions )','conditions',3,'p_conditions','grammar.py',406),
  ('conditions -> compare','conditions',1,'p_conditions','grammar.py',407),
  ('compare -> column COMPARISON item','compare',3,'p_compare','grammar.py',418),
  ('compare -> column like QSTRING','compare',3,'p_compare','grammar.py',419),
  ('compare -> column BETWEEN item AND item','compare',5,'p_compare','grammar.py',420),
  ('compare -> column IS null','compare',3,'p_compare','grammar.py',421),
  ('compare -> column in lritems','compare',3,'p_compare','grammar.py',422),
  ('lritems -> ( items )','lritems',3,'p_lritems','grammar.py',438),
  ('like -> LIKE','like',1,'p_like','grammar.py',443),
  ('like -> NOT LIKE','like',2,'p_like','grammar.py',444),
  ('in -> IN','in',1,'p_in','grammar.py',452),
  ('in -> NOT IN','in',2,'p_in','grammar.py',453),
  ('null -> NULL','null',1,'p_null','grammar.py',461),
  ('null -> NOT NULL','null',2,'p_null','grammar.py',462),
  ('empty -> <empty>','empty',0,'p_empty','grammar.py',472),
]