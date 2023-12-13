from flask import Flask,request,jsonify
import util
app=Flask(__name__)
@app.route('/get_loc_names')
def get_loc_names():
    response=jsonify({
        "locations":util.get_loc_names()
    })

    response.headers.add("Access-Control-Allow-origin","*")

    return response
@app.route('/predict_price', methods=['GET', 'POST'])
def predict_price():
    try:
        print(request.form)
        total_sqft= request.form["total_sqft"]
        print("hello")
        location= request.form["location"]
        bhk= request.form["bhk"]
        bath=request.form["bath"]
        estimate=util.get_estimated_price(location,float(total_sqft),int(bhk),int(bath))
        print(estimate)
        response=jsonify({
            "estimated_price":estimate
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(type(e))
        response=jsonify({"error":str(e)}) 
    response.headers.add("Access-Control-Allow-origin","*")
    return response 
if __name__=="__main__":
    print("Flask is running")
    util.load_saved_artifacts()
    app.run()