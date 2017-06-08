<h1>Manage e-mail accounts</h1>

<form action="processFormManageAccounts.php" method="post" target="_blank">
    <table>
        <tr>
            <td>
                Operation:
            </td>
            <td>
                <select name="operation">
                    <option value="Add">Add account</option>
                    <option value="Change">Change account</option>
                    <option value="Delete">Delete accounts</option>
                    <option value="List">List accounts</option>
                </select>
            </td>
        </tr>
    </table>

    <input type="submit" name="config" value="Done">
</form>
