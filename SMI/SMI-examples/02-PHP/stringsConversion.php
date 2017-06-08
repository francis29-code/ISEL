<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>PHP - Strings conversion</title>
  </head>
  <body>
    <?php
      $var1 = 1 + "10.5";
      $var2 = 1 + "-1.3e3";
      $var3 = 1 + "bob-1.3e3";
      $var4 = 1 + "bob3";
      $var5 = 1 + "10 Small Pigs";
      $var6 = 4 + "10.2 Little Piggies";
      $var7 = "10.0 pigs " + 1;
      $var8 = "pigs 10.0" + 1;
      $var9 = "10.0 pigs " + 1.0;
      $var10 = "10 pigs " + "4 dogs";
      
      echo "    <p>\$var1: $var1";
      echo "    <p>\$var2: $var2";
      echo "    <p>\$var3: $var3";
      echo "    <p>\$var4: $var4";
      echo "    <p>\$var5: $var5";
      echo "    <p>\$var6: $var6";
      echo "    <p>\$var7: $var7";
      echo "    <p>\$var8: $var8";
      echo "    <p>\$var9: $var9";
      echo "    <p>\$var10: $var10";
    ?>
  </body>
</html>
