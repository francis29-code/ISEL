<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>Update user profile - Forms App</title>

    <script type="text/javascript" src="scripts/forms.js">
    </script>
  </head>

  <body>
    <form 
      enctype="multipart/form-data"
      action="processUpdateProfile.php"
      method="POST"
      onsubmit="return FormUpdateProfileValidator(this)"
      name="FormUpdateProfile">

      Alias:<br>
      <input type="text" size="15" maxlength="15" name="alias"><br>

      Password:<br>
      <input type="password" size="15" maxlength="15" name="password"><br>

      Hobbies:<br>
      <table>
        <tr>
          <td>Cars<input type="checkbox" name="hobbyCars"></td>
          <td>Trains<input type="checkbox" name="hobbyTrains"></td>
        </tr>
      </table>

      Age:<br>
      <input type="radio" name="age" value="R1"> Less than 18<br>
      <input type="radio" name="age" value="R2"> More then 18 and less then 40<br>
      <input type="radio" name="age" value="R3"> More then 40 and less then 65<br>
      <input type="radio" name="age" value="R4"> More 65<br>

      Location:<br>
      <table>
        <tr>
          <td>
            District:<br>
            <select 
              onchange="SelectDistrictChange(this)" 
              name="district" 
              id="district" 
              size="1">
                <?php
                require_once( "../Lib/db.php" );
                
                dbConnect( ConfigFile );

                mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

                $query = "SELECT * FROM `smi`.`forms-districts`";
                $resultado = mysqli_query($GLOBALS['ligacao'], $query);

                if ($resultado) {
                  echo "<option value=\"0\"> </option>\n";
                  while ($registo = mysqli_fetch_array($resultado)) {
                    $id = $registo['idDistrict'];
                    $district = $registo['nameDistrict'];
                    echo "                <option value=\"$id\">$district</option>\n";
                  }
                }
                else {
                  echo "                <option value=\"-1\">No districts available</option>\n";
                }
                dbDisconnect();
                ?>
            </select><br>

            County:<br>
            <select 
              onchange="SelectCountyChange(this)"
              name="county" 
              id="county" 
              size="1">
            </select><br>

            Zip-code:<br>
            <select 
              name="zip" 
              id="zip" 
              size="1">
            </select><br>            
          </td>
          <td>
            <img id="imgDistrict" height="300" src="images/distritos/0.gif">
          </td>
        </tr>
      </table>

      Comments: (Please enter 200 characters maximum.)<br>
      <textarea name="comments" rows="4" cols="50"></textarea><br>
      
      <?php
        $MaxFileSize = 64*1024;
      ?>

      Photo (Max size <?php echo $MaxFileSize; ?>):<br>
      <input 
        type="hidden" 
        name="MAX_FILE_SIZE" 
        value="<?php echo $MaxFileSize; ?>">
      <input type="file" name="imagePhoto">
      <br>

      <input type="submit" name="Submit" value="Submit">
      <input type="reset" name="Reset" value="Reset"><p>
    </form>
  </body>
</html>