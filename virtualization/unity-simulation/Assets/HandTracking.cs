using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class HandTracking : MonoBehaviour
{
    // Start is called before the first frame update
    public UDPReceive udpReceive;
    public GameObject[] handPoints;
    public GameObject wholeHand;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string data = udpReceive.data;

        data = data.Remove(0, 1);
        data = data.Remove(data.Length - 1, 1);
        print(data);
        string[] points = data.Split(',');
        print(points[0]);

        float x0 = float.Parse(points[5 * 3 + 0]) - float.Parse(points[17 * 3 + 0]);
        float y0 = float.Parse(points[5 * 3 + 1]) - float.Parse(points[17 * 3 + 1]);
        float z0 = float.Parse(points[5 * 3 + 2]) - float.Parse(points[17 * 3 + 2]);
        float width_pix = Mathf.Sqrt(Mathf.Pow(x0, 2) + Mathf.Pow(y0, 2) + Mathf.Pow(z0, 2));

        float z_hand = -0.5f * width_pix + 40.0f;
        float hand_size = 50 / width_pix;

        wholeHand.transform.localScale = new Vector3(hand_size, hand_size, hand_size);
        wholeHand.transform.localPosition = new Vector3(0, 0, z_hand);

        for (int i = 0; i < 21; i++)
        {

            float x = 7 - float.Parse(points[i * 3]) / 25;
            float y = float.Parse(points[i * 3 + 1]) / 25;
            float z = float.Parse(points[i * 3 + 2]) / 25;

            handPoints[i].transform.localPosition = new Vector3(x, y, z);
            handPoints[i].transform.localScale = new Vector3(0.5f / hand_size, 0.5f / hand_size, 0.5f / hand_size);

        }
    }
}