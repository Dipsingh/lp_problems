/* sp-ex2.mod */

/* Decision variables */
var y12 <=10, >=0 ;
var y13 <=10, >=0 ;
var y23 <=15, >=0 ;

var x12 >=0 ;
var x132 >=0 ;
var x13 >=0 ;
var x123 >=0 ;
var x23 >=0 ;
var x213 >=0 ;



/* Objective function */
minimize PATH_COST: 5*x12 + 8*x13 + 2*x23 + 7*x24 + 4*x34 ;

/* Constraints */
s.t. NODE1: x12 + x13 = 1 ;
s.t. NODE2: x12 - x23 - x24 = 0 ;
s.t. NODE3: x13 + x23 - x34 = 0 ;

end;

