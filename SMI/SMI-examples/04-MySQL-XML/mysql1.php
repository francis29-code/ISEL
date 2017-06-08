<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>MySQL - Example 1</title>

    <link REL="stylesheet" TYPE="text/css" href="../Styles/GlobalStyle.css">
  </head>

  <body>

    <?php
    $linkIdentifier = mysqli_connect( "localhost:3306", "smi", "segredo" );

    mysqli_set_charset($linkIdentifier, 'utf8');

    mysqli_select_db($linkIdentifier, "smi");

    $query = "SELECT `idCounty`, `nameCounty` FROM `forms-counties` WHERE `idDistrict`='11'";

    $resultQuery = mysqli_query($linkIdentifier, $query);
    ?>

    <table border="1">
      <tr><th>id</th><th>county</th></tr>
<?php
      while ( ( $record = mysqli_fetch_array( $resultQuery ))) {

echo "        <tr>\n";
echo "          <td>" . $record['idCounty'] . "</td>\n";
echo "          <td>" . $record['nameCounty'] . "</td>\n";
echo "        </tr>\n";
      }
?>
    </table>
<?php
    mysqli_free_result( $resultQuery );
    mysqli_close( $linkIdentifier );
?>

  </body>

</html>