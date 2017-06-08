<h2>Add News</h2>

<form action="processFormAddNew.php" method="post" >
    <table>
        <tr>
            <td>
                Title
            </td>
            <td>
                <input type="text" name="title" value="Title">
            </td>
        </tr>

        <tr>
            <td>
                Autor
            </td>
            <td>
                <input type="text" name="author" value="Carlos Conçalves">
            </td>
        </tr>

        <tr>
            <td>
                Descripion
            </td>
            <td>
                <input type="text" name="description" value="This is the description">
            </td>
        </tr>
    </table>        

    <br>Contents<br>
    <?php
    try {
        $contents = @file_get_contents('http://loripsum.net/api/1/short/plaintext');

        if ($contents === false) {
            $contents = "An new example about RSS's is available";
        }
    } catch (Exception $e) {
        $contents = "An new example about RSS's is available";
    }
    ?>
    <textarea name="contents" rows="4" cols="50"><?php echo $contents ?></textarea><br><br>

    <input type="submit" name="submit" value="Publish"> 
    <input type="reset" name="reset" value="Clean">

</form>
