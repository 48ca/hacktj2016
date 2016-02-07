class SessionsController < ApplicationController
    def new
        
    end
    def create
        user = User.find_by(username: params[:session][:username].downcase)
        if user && user.authenticate(params[:session][:password])
            # Login user
        else
            flash[:danger] = "Invalid email/password combination"
            render 'new'
        end
    end
    def destroy
    end
end