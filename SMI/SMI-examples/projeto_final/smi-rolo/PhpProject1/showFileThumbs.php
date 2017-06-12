<?php
  require_once( "../Lib/lib.php" );
  require_once( "../Lib/db.php" );

  // TODO validate input data
  $id = $_GET['id'];

  // Read from the data base details about the file
  
  dbConnect(ConfigFile);
  mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);
  $query = "Select * from ficheiro where id ='".$id."'";
  $result = mysqli_query($GLOBALS['ligacao'], $query); 
  $result = mysqli_fetch_array($result);   
  

  $thumbFileNameAux = $result['conteudo_thumbs'];
  $thumbMimeFileName = $result['mime'];
  $thumbTypeFileName = $result['tipo'];

  header("Content-type: $thumbMimeFileName/$thumbTypeFileName");
  header("Content-Length: " . filesize($thumbFileNameAux));

  $thumbFileHandler = fopen($thumbFileNameAux, 'rb');
  //retorna toda a data de um apontador
  fpassthru($thumbFileHandler);
  fclose($thumbFileHandler);
  
  mysqli_free_result($result);
  dbDisconnect();
  
?>