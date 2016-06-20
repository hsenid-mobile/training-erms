package com.example.tharushashehan.ermsapp04;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;


public class InterviewRecord extends ActionBarActivity {

    private Button btnInterviewPerson01;
    private Button btnInterviewPerson02;
    private Button btnInterviewRecordBack;

  //  startActivity(new Intent(getApplicationContext(), InterviewRecord.class));

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_interview_record);

        btnInterviewRecordBack =(Button)findViewById(R.id.btnInterviewRecordBack);

        btnInterviewRecordBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),secondActivity.class));
            }
        });

        btnInterviewPerson01 = (Button)findViewById(R.id.btnInterviewPerson01);
        btnInterviewPerson02 = (Button)findViewById(R.id.btnInterviewPerson02);

        //delete this
        btnInterviewPerson01.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),iterviewPerson.class));
            }
        });

        btnInterviewPerson02.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(), iterviewPerson.class));
            }
        });
        // to this

    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_interview_record, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
