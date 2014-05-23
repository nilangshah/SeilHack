<html>
<body>
<?php
$db = pg_connect("","","","","marks_db");

$query1 = "SELECT table_schema,table_name FROM information_schema.tables where table_schema='public'";
$result1 = pg_exec($db, $query1);
if (!$result1) {
	printf ("ERROR"); exit;
}

$i1 = 0;
$row1 = pg_fetch_row ($result1,$i1);

while($row1){
	$query = "SELECT count(*) FROM $row1[1]";
	$result = pg_exec($db, $query);
	if (!$result) {printf ("ERROR"); exit;}
	$i=0;
	$row = pg_fetch_row ($result,$i);
	printf ("Rows in %s : %s<br>\n",$row1[1] ,$row[0]);

	$i1=$i1+1;
	$row1 = pg_fetch_row ($result1,$i1);
}

pg_close($db);
?>
</body>
</html>
