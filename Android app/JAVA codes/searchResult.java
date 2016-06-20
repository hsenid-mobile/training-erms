package com.example.tharushashehan.ermsapp04;

import android.content.Intent;
import android.support.annotation.StringDef;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;


public class searchResult extends ActionBarActivity {

    private EditText txtSearchName, txtSearchdegree, txtSearchPost;
    private Button btnSearchResultBack;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search_result);
        btnSearchResultBack =(Button) findViewById(R.id.btnSearchResultBack);

        btnSearchResultBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),secondActivity.class));
            }
        });

    }

    protected String doInBackground(String... params){
        String content=HttpManager.getData("http://192.168.56.1:8080/android/");
        return content;
    }

    protected void onPostExecute(String s){

        String[] word = s.split(s);
        txtSearchName.setText(s);
        txtSearchdegree.setText(s);
        txtSearchPost.setText(s);
    }

   /** @Override
    public boolean onCreateOptionsMenu(Menu menu) {

        getMenuInflater().inflate(R.menu.menu_search_result, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        int id = item.getItemId();

        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }**/
}
