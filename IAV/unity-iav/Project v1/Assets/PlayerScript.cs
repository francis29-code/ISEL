using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerScript : MonoBehaviour {

    public float speed = 6f;

    Vector3 movement;
    Rigidbody pRigid;
    int floorMask;
    float camRayLenght;

	// Use this for initialization
	void Awake () {
        pRigid = GetComponent<Rigidbody>();
        floorMask = LayerMask.GetMask("Floor");
    }
	
	// Update is called once per frame
	void FixedUpdate () {
        float h = Input.GetAxisRaw("Horizontal");
        float v = Input.GetAxisRaw("Vertical");

        Move (h,v);
        turning();
	}

    private void Move(float h, float v)
    {
        movement.Set(h,0f,v);

        movement = movement.normalized * speed * Time.deltaTime;

        pRigid.MovePosition(transform.position + movement);

    }

    void turning()
    {
        //Ray camRay = Camera.main.ScreenPointToRay(Input.mousePosition);
        //RaycastHit floorHit;

        //if (Physics.Raycast(camRay, out floorHit, camRayLenght, floorMask))
        //{
        //    Vector3 playerToMouse = floorHit.point - transform.position;
        //    playerToMouse.y = 0f;
        //
        //    Quaternion newRot = Quaternion.LookRotation(playerToMouse);
        //    pRigid.MoveRotation(newRot);
        //}
        Vector3 pos = Input.mousePosition;
        
        transform.LookAt(pos);
        
    }
}
