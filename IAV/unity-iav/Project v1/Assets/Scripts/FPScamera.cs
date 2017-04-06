using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FPScamera : MonoBehaviour {
    public Transform target;
    public float smoothing = 5f;
    Vector3 offset;
    Quaternion rot;
	// Use this for initialization
	void Start () {
        offset = transform.position - target.position;
        
	}
	
	// Update is called once per frame
	void Update () {
        Vector3 targetCamPos = target.position + offset;
        //mexe-se de acordo com o inimigo fluidamente pelo uso de Lerp
        transform.position = Vector3.Lerp(transform.position, targetCamPos, smoothing * Time.deltaTime);
     
        transform.LookAt(target);
	}
}
