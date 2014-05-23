<?php

  $date1 = $_GET['date'];
// Path to the python script - either FULL path or relative to PHP script
  $pythonScript = 'test_kresit.py';

  // Path to python executable  - either FULL path or relative to PHP script
  $pythonExec = '/usr/bin/python';
 exec("$pythonExec \"$pythonScript\" $date1 2>&1", $output);


$file1 = fopen("kresit_energy_vs_temprature.csv","r");

$unit1 = "kWh";
$unit2 = "°C";
$line=fgetcsv($file1);
while($line=fgetcsv($file1))
{
	$categories[] = $line[0];
	$energy[] = floatval($line[1]/1000);
	$temperature[] = floatval($line[2]);
}
$data = array(array("name"=>"Energy","value"=>$energy),array("name"=>"Temperature","value"=>$temperature));
$arr = array("days"=>$categories,"unit1"=>$unit1,"unit2"=>$unit2,"components"=>$data);
echo json_encode($arr); 
?>
