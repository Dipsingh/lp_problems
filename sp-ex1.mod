/* sp-ex1.mod */

/* Decision variables */
var x12 <=1, >=0 ;
var x13 <=1, >=0 ;
var x23 <=1, >=0 ;
var x24 <=1, >=0 ;
var x34 <=1, >=0 ;

/* Objective function */
minimize PATH_COST: 5*x12 + 8*x13 + 2*x23 + 7*x24 + 4*x34 ;

/* Constraints */
s.t. NODE1: x12 + x13 = 1 ;
s.t. NODE2: x12 - x23 - x24 = 0 ;
s.t. NODE3: x13 + x23 - x34 = 0 ;

end;

