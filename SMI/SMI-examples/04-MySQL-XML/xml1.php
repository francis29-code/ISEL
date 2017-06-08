<?php
  header('Content-Type: text/html; charset=utf-8');
  
  $data = <<<XML
<?xml version="1.0"?>
<DataBase>
  <Host>localhost</Host>
  <Port>3306</Port>
  <DB>smi</DB>
  <Username>smi</Username>
  <Password>segredo</Password>
</DataBase>
XML;

  $xmld = simplexml_load_string( $data );
  
  $fileName = "file.xml";
  
  file_put_contents( $fileName, $xmld->asXML() );
  
  echo "XML was writen to \"$fileName\"";
?>