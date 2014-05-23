<?php
$duration = $_GET['duration'];
$type = $_GET['parameter'];

$output = passthru("/usr/bin/python \"kresit_master_data.py\" $duration $type ");
//echo json_encode($output);
?>
