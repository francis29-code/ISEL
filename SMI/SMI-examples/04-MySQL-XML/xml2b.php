<?php
  header('Content-Type: text/html; charset=utf-8');
  
  $students = simplexml_load_file( "students.xml" );
  
  #echo "<pre>";
  #print_r( $students );
  #echo "</pre>";
  
  echo "Name of the 1st student:\n<br>";
  echo $students->Student[0]->Name . "\n<br><br>";
  
  echo "Show all the students:\n<br>";
  foreach ($students->Student as $student) {
  	echo "Name: " . $student->Name . "\n<br>";
  	echo "Filiation:\n<br>";
  	echo "Father: " . $student->Filiation->Father . "\n<br>";
  	echo "Mother: " . $student->Filiation->Mother . "\n<br>";
    
    echo "<ul>";
    echo "\n<br>IC - 1stMode - Using the attributs:\n<br>";
    echo "Number: " . $student->ic . "\n<br>";
    echo "Date: " . $student->ic[ 'date' ] . "\n<br>";
    echo "City: " . $student->ic[ 'city' ] . "\n<br>";
    
    echo "\n<br>IC - 2nd Mode - foreach:\n<br>";
    $attributesIC = get_object_vars( $student->ic );
    echo "Number: " . $student->ic . "\n<br>";
    foreach( $attributesIC as $k1 => $v1 ) {
      foreach($v1 as $k2 => $v2 ) {
        echo "IC[ $k2 ] -> $v2\n<br>";
      }
    }
    echo "</ul>";
    
    echo "\n<br>E-mail: " . $student->email. "\n<br><br>";
  }
?>