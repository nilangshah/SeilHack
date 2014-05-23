<form action="exer1.php" method="post">
    Roll No:<br>
    <input type="text" name="rollno"><br><br>
    Password:<br>
    <input type="password" name="password"><br><br>
    <input type="submit" name="submit" value="Login">
</form>
 <?php
if(isset($_POST['submit'])){
$db = pg_connect("","","","","marks_db");


$rollNo=trim($_POST["rollno"]);
$password=trim($_POST["password"]);

$query = "SELECT password FROM users where RollNo='$rollNo'";
$result = pg_exec($db, $query);
if (!$result) {printf ("ERROR in db connection"); exit;}
$row = pg_fetch_row ($result,$i);
if(!$row){printf("Rollno does not exist");exit;}

if($password==$row[0])
{  	session_start(); 
 	$_SESSION['rollno'] = $rollNo;
        $_SESSION['logged'] = TRUE; 

header("Location: http://localhost/verify.php");

}
else
{printf ("password incorrect<br>\n");
}

pg_close($db);

}
?> 

