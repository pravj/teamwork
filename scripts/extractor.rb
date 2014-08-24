require 'yaml'
require 'json'

language_file = File.join(File.dirname(__FILE__), 'languages.yml')
language_data = YAML.load_file(language_file)

color_data = Hash.new

language_data.each do |language|
  if language[1]['color']
    color_data[language[0]] = language[1]['color']
  end
end

color_file_path = File.join(File.dirname(__FILE__), '../raw/languages.json')
color_file = File.open(color_file_path, 'w')
color_file.write(color_data.to_json)
