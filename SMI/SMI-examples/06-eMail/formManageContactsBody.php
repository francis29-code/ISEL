<h1>Manage e-mail contacts</h1>

<form action="processFormManageContacts.php" method="post" target="_blank">
    <table>
        <tr>
            <td>
                Operation:
            </td>
            <td>
                <select name="operation">
                    <option value="Add">Add contact</option>
                    <option value="Change">Change contact</option>
                    <option value="Delete">Delete contact</option>
                    <option value="List">List contacts</option>
                </select>
            </td>
        </tr>
    </table>

    <input type="submit" name="config" value="Done">
</form>
