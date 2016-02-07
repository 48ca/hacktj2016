class UsersController < ApplicationController
    def index
        # Perhaps unused
    end
    def show
        @user = User.find_by_id(params[:id])
    end
    def create
        @user = User.new(user_params)
        if @user.save
            redirect_to @user
        else
            flash[:danger] = "Creation failed!"
            render 'new'
        end
    end
    def new
    end
    def destroy
    end
    private
        def user_params
            params.require(:user).permit(:username,:password_digest)
        end
end
