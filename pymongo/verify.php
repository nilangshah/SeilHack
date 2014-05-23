<?php
session_start();
if(!$_SESSION['logged']){
    header("Location: http://localhost/exer1.php");
    exit;
}

$db = pg_connect("","","","","marks_db");

$rollNo = $_SESSION['rollno'];

$query = "SELECT * FROM marks where RollNo='$rollNo'";


$result2 = pg_exec($db, $query);


if (!$result2) {printf ("ERROR in db connection <br> \n"); exit;}

$row = pg_fetch_row ($result2,0);

if(!$row){printf("Marks yet not updated<br>\n");exit;}
else
{
printf("Quiz1 :%s <br> \n",$row[1]);
printf("Midsem :%s <br> \n",$row[2]);
printf("Quiz2 :%s <br> \n",$row[3]);
printf("Project :%s <br> \n",$row[4]);
printf("Endsem :%s <br> \n",$row[5]);

}
exit;

?> 

