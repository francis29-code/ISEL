<?php
require_once( "../Lib/db.php");

dbConnect(ConfigFile);

$db = $GLOBALS['configDataBase']->db;

mysqli_select_db($GLOBALS['ligacao'], $db);
?>

<h1>Send an e-mail using PHP mail function</h1>

<form action="processFormSendPHP.php" method="post" target="_blank">
    <table>
        <tr>
            <td>
                * Account:
            </td>
            <td>
                <select name="accountId">
                    <?php
                    $queryAccounts = "SELECT `id`, `accountName` FROM `smi`.`email-accounts`";
                    $resultAccounts = mysqli_query($GLOBALS['ligacao'], $queryAccounts);

                    if ($resultAccounts) {
                        while ($registoAccounts = mysqli_fetch_array($resultAccounts)) {
                            $accountId = $registoAccounts['id'];
                            $accountName = $registoAccounts['accountName'];
                            echo "                <option value=\"$accountId\">$accountName</option>\n";
                        }

                        mysqli_free_result($resultAccounts);
                    } else {
                        echo "                <option value=\"-1\">No e-mail accounts available</option>\n";
                    }
                    ?>
                </select>
            </td>
        </tr>

        <tr>
            <td>
                <table>
                    <tr>
                        <td>
                            Contacts
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <select name="contactId">
                                <?php
                                $queryContacts = "SELECT `id`, `displayName` FROM `smi`.`email-contacts`";
                                $resultContacts = mysqli_query($GLOBALS['ligacao'], $queryContacts);
                                if ($resultContacts) {
                                    echo "                <option value=\"0\"></option>\n";
                                    while ($registoContacts = mysqli_fetch_array($resultContacts)) {
                                        $contactId = $registoContacts['id'];
                                        $fromName = $registoContacts['displayName'];
                                        echo "                <option value=\"$contactId\">$fromName</option>\n";
                                    }
                                    mysqli_free_result($resultContacts);
                                } else {
                                    echo "                <option value=\"-1\">No e-mail contacts available</option>\n";
                                }
                                ?>
                            </select>
                        </td>
                    </tr>

                </table>
            </td>
            <td>
                <table>
                    <tr>
                        <td>
                            * To... 
                        </td>
                        <td>
                            <input onclick="addAddress('contactId', 'toList')" type="button" value=">>">
                        </td>
                        <td>
                            <input type="text" size="80" name="toList">
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Cc...
                        </td>
                        <td>
                            <input onclick="addAddress('contactId', 'ccList')" type="button" value=">>">
                        </td>
                        <td>
                            <input type="text" size="80" name="ccList">
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Bcc...
                        </td>
                        <td>
                            <input onclick="addAddress('contactId', 'bccList')" type="button" value=">>">
                        </td>
                        <td>
                            <input type="text" size="80" name="bccList">
                        </td>
                    </tr>
                </table>
            </td>
        </tr>

        <tr>
            <td>
                * Subject:
            </td>
            <td>
                <input type="text" size=32 name="subject" value="Email Subject">
            </td>
        </tr>

        <tr>
            <td>
                * Message:
            </td>
            <td>
                <textarea name="message" rows="4" cols="50">Test message using PHP</textarea>
            </td>
        </tr>
    </table>
    <br>

    <input type="submit" name="send" value="Send E-mail"> <input type="reset" name="reset" value="Clear">

    <br>
    The fields marked with a * are mandatory.
</form>
