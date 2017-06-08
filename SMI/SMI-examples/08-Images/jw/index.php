<?php
  require_once( "../../Lib/lib.php" );
  
  $name = webAppName();
  
  require_once( "../config.php" );
?>
<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    
    <script type="text/javascript" src="<?php echo $jwplayerScript;?>" ></script>
    <script type="text/javascript">jwplayer.key="vcwcUyC5+6Vt4//CWqA75J1tVcD3wQTRLcZN5g==";</script>
  </head>
  
  <body>
    <div id="myElement">Loading the player ...</div>
    <script type="text/javascript">
    jwplayer("myElement").setup({
          autostart: "false",
          author: "Carlos Gonçalves",
          date: "<?php echo date('F d Y'); ?>",
          height: 480,
          width: 640,
          playlist: [{
              title: "out.mp4",
              description: "Ficheiro de vídeo no formato mp4",
              image: "<?php echo $name; ?>out.jpg",
              sources: [
                { 
                  file: "<?php echo $name; ?>out.mp4",
                  type: "mp4"
                }
              ]
          }]          
    });
</script>
  </body>
</html>
    