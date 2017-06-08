<!DOCTYPE html>
<?php
header('Content-Type: text/html; charset=utf-8');

if ( isset($_POST['alias']) ) {
  echo "Alias: " . $_POST['alias'] . "<br>\n";
}

if ( isset($_POST['password']) ) {
  echo "Password: " . $_POST['password'] . "<br>\n";
}

if ( isset($_POST['hobbyCars']) ) {
  echo "hobbyCars: " . $_POST['hobbyCars'] . "<br>\n";
}

if ( isset($_POST['hobbyTrains']) ) {
  echo "hobbyTrains: " . $_POST['hobbyTrains'] . "<br>\n";
}

if ( isset($_POST['age']) ) {
  echo "Age: " . $_POST['age'] . "<br>\n";
}

if ( isset($_POST['district']) ) {
  echo "District: " . $_POST['district'] . "<br>\n";
}

if ( isset($_POST['county']) ) {
  echo "County: " . $_POST['county'] . "<br>\n";
}

if ( isset($_POST['zip']) ) {
  echo "Zip-Code: " . $_POST['zip'] . "<br>\n";
}

echo "<pre>";
print_r($_FILES);
echo "<pre>";

// Maximum time allowed for the upload
set_time_limit(60);

// Name of the upload file in the temporary directory
$source = $_FILES['imagePhoto']['tmp_name'];
// Original name of the file that was uploaded
$sourceName = $_FILES['imagePhoto']['name'];

if (($sourceName <> "none") && ($sourceName <> "" )) {
  // Directory where the file will be placed
  $dest = "C:\\Temp\\upload\\";
  // Destination for the uploaded file
  $destName = $dest . $sourceName;

  echo "File: $source<br>\n";
  echo "Original name of the file: $sourceName<br>\n";
  echo "Destination directory: $dest<br>\n";
  echo "Full destination name: $destName<br>\n";

  if (copy($source, $destName)) {
    unlink($source);
    $destName = addslashes($destName);
    echo "Destination name with slashes: $destName<br>\n";
  } else {
    echo "Could not write file to $dest";
  }
} else {
  echo "Picture file not specified.<br>";
}
?>
