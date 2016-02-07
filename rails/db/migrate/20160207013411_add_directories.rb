class AddDirectories < ActiveRecord::Migration
  def change
    change_table :users do |t|
      t.string :music_directory
      t.string :photos_directory
    end
  end
end
