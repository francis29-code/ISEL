<!DOCTYPE html>
<?php
header('Content-Type: text/html; charset=utf-8');

$district = $_GET["district"];

$options = "";

require_once( "../Lib/db.php" );

dbConnect(ConfigFile);

mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

$query = "SELECT `idCounty`, `nameCounty` FROM `forms-counties` WHERE `idDistrict`=$district";
$resultado = mysqli_query($GLOBALS['ligacao'], $query);
$notFirst = FALSE;

if ($resultado) {
  $options .= "0| @";
  while ($registo = mysqli_fetch_array($resultado)) {
    $id = $registo['idCounty'];
    $county = $registo['nameCounty'];
    if ($notFirst) {
      $options .= "@";
    } else {
      $notFirst = TRUE;
    }
    $options .= "$id|$county";
  }
} else {
  $options = '-1|No Counties Available';
}
dbDisconnect();

echo $options;
?>
