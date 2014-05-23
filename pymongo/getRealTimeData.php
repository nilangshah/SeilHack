<?php
  $pythonScript = "kresit_realtime.py";
  $pythonExec = '/usr/bin/python';
  //$output = 
  exec("$pythonExec \"$pythonScript\"", $output);
  echo substr(stripslashes(json_encode($output)),2,-2);
?>
