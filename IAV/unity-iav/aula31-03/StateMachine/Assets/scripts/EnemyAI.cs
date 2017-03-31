using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyAI : MonoBehaviour {

	//atribuir publico permite modificar na interface do UNITY
	//neste casa associar um player a este SCRIPT
	public Transform player;
	public Transform[] waypoint;
	public float speed = 2;
	private Animator anim;
	private int currentTarget = 0;
	private Rigidbody rb;

	// Use this for initialization
	private void Start () {
		//referencia para a maquina de estados
		anim = GetComponent<Animator> ();
		rb = GetComponent<Rigidbody> ();
	}

	// Update is called once per frame
	private void Update () {
		float dist = Vector3.Distance (transform.position,player.position);
		anim.SetFloat ("distToPlayer", dist);

		Vector3 target = waypoint [currentTarget].position;

		dist = Vector3.Distance (transform.position, target);
		anim.SetFloat ("distToTarget",dist);

		Vector3 direction = target - transform.position;

		rb.MovePosition (transform.position + direction.normalized * Time.deltaTime * speed);

	}

	public void nextTarget (){
		currentTarget = (currentTarget + 1) % waypoint.Length;
	}
}
