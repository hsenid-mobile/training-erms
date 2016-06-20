package com.example.tharushashehan.ermsapp04;

import android.util.Log;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;

/**
 * Created by Tharusha Shehan on 6/12/2016.
 */
public class HttpJsonParser {

    public static String getData(String url_select) {

        //This has been finalized no need to edit anymore.


        ArrayList<NameValuePair> param = new ArrayList<NameValuePair>();
        InputStream inputStream = null;
        StringBuilder sBuilder = new StringBuilder();

        try {
            // Set up HTTP post
            // HttpClient is more then less deprecated. Need to change to URLConnection
            HttpClient httpClient = new DefaultHttpClient();

            HttpPost httpPost = new HttpPost(url_select);
            httpPost.setEntity(new UrlEncodedFormEntity(param));
            HttpResponse httpResponse = httpClient.execute(httpPost);
            HttpEntity httpEntity = httpResponse.getEntity();

            // Read content & Log
            inputStream = httpEntity.getContent();
        } catch (UnsupportedEncodingException e1) {
            Log.e("UnsupportedEncodingException", e1.toString());
            e1.printStackTrace();
        } catch (ClientProtocolException e2) {
            Log.e("ClientProtocolException", e2.toString());
            e2.printStackTrace();
        } catch (IllegalStateException e3) {
            Log.e("IllegalStateException", e3.toString());
            e3.printStackTrace();
        } catch (IOException e4) {
            Log.e("IOException", e4.toString());
            e4.printStackTrace();
        }
        // Convert response to string using String Builder
        try {
            BufferedReader bReader = new BufferedReader(new InputStreamReader(inputStream, "utf-8"), 8);
            //StringBuilder sBuilder = new StringBuilder();

            String line = null;
            while ((line = bReader.readLine()) != null) {
                sBuilder.append(line + "\n");
            }
            inputStream.close();

        } catch (Exception e) {
            Log.e("StringBuilding & BufferedReader", "Error converting result " + e.toString());
        }
    return sBuilder.toString();
}
}