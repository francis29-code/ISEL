using UnityEngine;
using System.Collections;

public class Game : MonoBehaviour
{
	Player player;

	// Use this for initialization
	void Start ()
	{
		player = new Player ();
		int x = 10;
		player.Experience = x;
		print (player.Experience);
	}
	
	// Update is called once per frame
	void Update ()
	{
	
	}
}

