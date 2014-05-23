<?php

//$abc = passthru("./test_lab1.py");
/*
$file1 = fopen("appliance_energy_data1.csv","r");

$labname= "SEIL";

$unit = "kWh";
$line=fgetcsv($file1);
while($line=fgetcsv($file1))
{
	$categories[] = $line[0];
	$ac[] = floatval($line[1]);
	$pc[] = floatval($line[2]);
	$light[] = floatval($line[3]);
	$total[] = $line[4];
	$average[] = ($line[1] + $line[2] + $line[3]) / 3;
}
$data = array(array("name"=>"AC","values"=>$ac,"total"=>array_sum($ac)),array("name"=>"PC and Sockets","values"=>$pc,"total"=>array_sum($pc)),array("name"=>"Lights and fans","values"=>$light,"total"=>array_sum($light)));
$arr = array("days"=>$categories,"lab"=>$labname,"unit"=>$unit,"appliances"=>array("AC","PC and Sockets","Lights and fans"),"components"=>$data,"averages"=>$average);
echo json_encode($arr);*/ 


  // Path to the python script - either FULL path or relative to PHP script
 $date1 = $_GET['date'];
 
  $pythonScript = 'test_lab1.py';

  // Path to python executable  - either FULL path or relative to PHP script
  $pythonExec = '/usr/bin/python';

  // Check the file exists and PHP has permission to execute it
  clearstatcache();
  if (!file_exists($pythonExec)) {
    exit("The python executable '$pythonExec' does not exist!");
  }
  if (!is_executable($pythonExec)) {
    exit(("The python executable '$pythonExec' is not executable!"));
  }
  if (!file_exists($pythonScript)) {
    exit("The python script file '$pythonScript' does not exist!");
  }

  // Execute it, and redirect STDERR to STDOUT so we can see error messages as well
  exec("$pythonExec \"$pythonScript\" $date1 2>&1", $output);

  
  $file1 = fopen("appliance_energy_data1.csv","r");

$labname= "SEIL";

$unit = "kWh";
$line=fgetcsv($file1);
while($line=fgetcsv($file1))
{
	$categories[] = $line[0];
	$ac[] = floatval($line[1]);
	$pc[] = floatval($line[2]);
	$light[] = floatval($line[3]);
	$total[] = $line[4];
	$average[] = ($line[1] + $line[2] + $line[3]) / 3;
}
$data = array(array("name"=>"AC","values"=>$ac,"total"=>array_sum($ac)),array("name"=>"PC and Sockets","values"=>$pc,"total"=>array_sum($pc)),array("name"=>"Lights and fans","values"=>$light,"total"=>array_sum($light)));
$arr = array("days"=>$categories,"lab"=>$labname,"unit"=>$unit,"appliances"=>array("AC","PC and Sockets","Lights and fans"),"components"=>$data,"averages"=>$average);
echo json_encode($arr);


?>
