package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class MyItem {

    private final String title;
    private final String description;
    private final String url;

    public MyItem(JSONObject data) throws JSONException {

        this.title = data.getString("name");
        this.description = data.getString("description");
        this.url = data.getString("image_url");

    }
    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public String getUrl() {
        return url;
    }
}
