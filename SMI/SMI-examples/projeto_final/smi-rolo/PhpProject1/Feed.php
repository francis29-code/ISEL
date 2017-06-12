<?php
  require_once( "../Lib/lib.php" );
  require_once( "../Lib/db.php" );

  $numColls = 0 + 3;

  // Read from the data base the list of the files
  dbConnect(ConfigFile);
  mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);
  //falta escolher qual o username apresentar o feed
  // IDEIA => $_SESSION['username']
  $query = "Select id from ficheiro";
  $result = mysqli_query($GLOBALS['ligacao'], $query);
?>

<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>List Images</title>
  </head>

  <body>
    <h1 align="center">Files available</h1>

    <table border="1" align="center" cellspacing="10">

      <?php
      $currCol = 1;

      while ($imageData = mysqli_fetch_array($result)) {
        $id = $imageData["id"];


        if ($currCol == 1) {
          echo "<tr>\n";
        }
        $target = "<img src=\"showFileThumbs.php?id=$id\">";
        //print_r($target);
        echo "<td><a '>$target</a></td>\n";
        //href='showFile.php?nome=$nome

        if ($currCol == $numColls) {
          echo "</tr>\n";
          $currCol = 1;
        } else {
          ++$currCol;
        }
      }

      mysqli_free_result($result);
      dbDisconnect();
      ?>

    </table>
  </body>
</html>
