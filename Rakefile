# frozen_string_literal: true

require "etc"

$root = Pathname.new(__FILE__).dirname.realpath
$lib = $root / "lib"

require "ruby-progressbar"
require "yard"
require "minitest/test_task"

require_relative $root / "lib" / "validate"

directory "#{$root}/.stamps"

Dir.glob("#{$root}/backends/*/tasks.rake") do |rakefile|
  load rakefile
end

directory "#{$root}/.stamps"

file "#{$root}/.stamps/dev_gems" => "#{$root}/.stamps" do
  Dir.chdir($root) do
    sh "bundle config set --local with development"
    sh "bundle install"
    FileUtils.touch "#{$root}/.stamps/dev_gems"
  end
end

namespace :gen do
  desc "Generate documentation for the ruby tooling"
  task tool_doc: "#{$root}/.stamps/dev_gems" do
    Dir.chdir($root) do
      sh "bundle exec yard doc --yardopts arch_def.yardopts"
      sh "bundle exec yard doc --yardopts idl.yardopts"
    end
  end
end

namespace :serve do
  desc <<~DESC
    Start an HTML server to view the generated HTML documentation for the tool

    The default port is 8000, though it can be overridden with an argument
  DESC
  task :tool_doc, [:port] => "gen:tool_doc" do |_t, args|
    args.with_defaults(port: 8000)

    puts <<~MSG
      Server will come up on http://#{`hostname`.strip}:#{args[:port]}.
      It will regenerate the documentation on every access

    MSG
    sh "yard server -p #{args[:port]} --reload"
  end
end

namespace :test do
  # "Run the IDL compiler test suite"
  task :idl_compiler do
    t = Minitest::TestTask.new(:lib_test)
    t.test_globs = ["#{$root}/lib/idl/tests/test_*.rb"]
    t.process_env
    ruby t.make_test_cmd
  end

  # "Run the Ruby library test suite"
  task :lib do
    t = Minitest::TestTask.new(:lib_test)
    t.test_globs = ["#{$root}/lib/test/test_*.rb"]
    t.process_env
    ruby t.make_test_cmd
  end
end

desc "Clean up all generated files"
task :clean do
  FileUtils.rm_rf $root / "gen"
  FileUtils.rm_rf $root / ".stamps"
end

namespace :test do
  task :insts do
    puts "Checking instruction encodings..."
    inst_paths = Dir.glob("#{$root}/arch/inst/**/*.yaml").map { |f| Pathname.new(f) }
    inst_paths.each do |inst_path|
      Validator.instance.validate_instruction(inst_path)
    end
    puts "All instruction encodings pass basic sanity tests"
  end
  task schema: "gen:arch" do
    validator = Validator.instance
    puts "Checking arch files against schema.."
    arch_files = Dir.glob("#{$root}/arch/**/*.yaml")
    progressbar = ProgressBar.create(total: arch_files.size)
    arch_files.each do |f|
      progressbar.increment
      validator.validate(f)
    end
    Rake::Task["test:insts"].invoke
    puts "All files validate against their schema"  
  end
  task idl_model: ["gen:arch", "#{$root}/.stamps/arch-gen-_32.stamp", "#{$root}/.stamps/arch-gen-_64.stamp"]  do
    print "Parsing IDL code for RV32..."
    arch_def_32 = arch_def_for("_32")
    puts "done"

    arch_def_32.type_check

    print "Parsing IDL code for RV64..."
    arch_def_64 = arch_def_for("_64")
    puts "done"

    arch_def_64.type_check

    puts "All IDL passed type checking"
  end
end

def insert_warning(str, from)
  # insert a warning on the second line
  lines = str.lines
  first_line = lines.shift
  lines.unshift(first_line, "\n# WARNING: This file is auto-generated from #{Pathname.new(from).relative_path_from($root)}\n\n").join("")
end
private :insert_warning

(3..31).each do |hpm_num|
  file "#{$root}/arch/csr/Zihpm/mhpmcounter#{hpm_num}.yaml" => [
    "#{$root}/arch/csr/Zihpm/mhpmcounterN.layout",
    __FILE__
   ] do |t|
    puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
    erb = ERB.new(File.read($root / "arch/csr/Zihpm/mhpmcounterN.layout"), trim_mode: "-")
    erb.filename = "#{$root}/arch/csr/Zihpm/mhpmcounterN.layout"
    File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
  end
  file "#{$root}/arch/csr/Zihpm/mhpmcounter#{hpm_num}h.yaml" => [
    "#{$root}/arch/csr/Zihpm/mhpmcounterNh.layout",
    __FILE__
   ] do |t|
    puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
    erb = ERB.new(File.read($root / "arch/csr/Zihpm/mhpmcounterNh.layout"), trim_mode: "-")
    erb.filename = "#{$root}/arch/csr/Zihpm/mhpmcounterNh.layout"
    File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
  end
  file "#{$root}/arch/csr/Zihpm/mhpmevent#{hpm_num}.yaml" => [
    "#{$root}/arch/csr/Zihpm/mhpmeventN.layout",
    __FILE__
   ] do |t|
    puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
    erb = ERB.new(File.read($root / "arch/csr/Zihpm/mhpmeventN.layout"), trim_mode: "-")
    erb.filename = "#{$root}/arch/csr/Zihpm/mhpmeventN.layout"
    File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
  end
  file "#{$root}/arch/csr/Zihpm/mhpmevent#{hpm_num}h.yaml" => [
    "#{$root}/arch/csr/Zihpm/mhpmeventNh.layout",
    __FILE__
   ] do |t|
    puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
    erb = ERB.new(File.read($root / "arch/csr/Zihpm/mhpmeventNh.layout"), trim_mode: "-")
    erb.filename = "#{$root}/arch/csr/Zihpm/mhpmeventNh.layout"
    File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
  end
  file "#{$root}/arch/csr/Zihpm/hpmcounter#{hpm_num}.yaml" => [
    "#{$root}/arch/csr/Zihpm/hpmcounterN.layout",
    __FILE__
   ] do |t|
    puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
    erb = ERB.new(File.read($root / "arch/csr/Zihpm/hpmcounterN.layout"), trim_mode: "-")
    erb.filename = "#{$root}/arch/csr/Zihpm/hpmcounterN.layout"
    File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
  end
  file "#{$root}/arch/csr/Zihpm/hpmcounter#{hpm_num}h.yaml" => [
    "#{$root}/arch/csr/Zihpm/hpmcounterNh.layout",
    __FILE__
    ] do |t|
    puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
    erb = ERB.new(File.read($root / "arch/csr/Zihpm/hpmcounterNh.layout"), trim_mode: "-")
    erb.filename = "#{$root}/arch/csr/Zihpm/hpmcounterNh.layout"
    File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
  end
end

(0..63).each do |pmpaddr_num|
  file "#{$root}/arch/csr/I/pmpaddr#{pmpaddr_num}.yaml" => [
    "#{$root}/arch/csr/I/pmpaddrN.layout",
    __FILE__
   ] do |t|
    puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
    erb = ERB.new(File.read($root / "arch/csr/I/pmpaddrN.layout"), trim_mode: "-")
    erb.filename = "#{$root}/arch/csr/I/pmpaddrN.layout"
    File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
  end
end

(0..15).each do |pmpcfg_num|
  file "#{$root}/arch/csr/I/pmpcfg#{pmpcfg_num}.yaml" => [
    "#{$root}/arch/csr/I/pmpcfgN.layout",
    __FILE__
   ] do |t|
    puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
    erb = ERB.new(File.read($root / "arch/csr/I/pmpcfgN.layout"), trim_mode: "-")
    erb.filename = "#{$root}/arch/csr/I/pmpcfgN.layout"
    File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
  end
end

file "#{$root}/arch/csr/I/mcounteren.yaml" => [
  "#{$root}/arch/csr/I/mcounteren.layout",
  __FILE__
] do |t|
  puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
  erb = ERB.new(File.read($root / "arch/csr/I/mcounteren.layout"), trim_mode: "-")
  erb.filename = "#{$root}/arch/csr/I/mcounteren.layout"
  File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
end

file "#{$root}/arch/csr/S/scounteren.yaml" => [
  "#{$root}/arch/csr/S/scounteren.layout",
  __FILE__
] do |t|
  puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
  erb = ERB.new(File.read($root / "arch/csr/S/scounteren.layout"), trim_mode: "-")
  erb.filename = "#{$root}/arch/csr/S/scounteren.layout"
  File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
end

file "#{$root}/arch/csr/H/hcounteren.yaml" => [
  "#{$root}/arch/csr/H/hcounteren.layout",
  __FILE__
] do |t|
  puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
  erb = ERB.new(File.read($root / "arch/csr/H/hcounteren.layout"), trim_mode: "-")
  erb.filename = "#{$root}/arch/csr/H/hcounteren.layout"
  File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
end

file "#{$root}/arch/csr/Zicntr/mcountinhibit.yaml" => [
  "#{$root}/arch/csr/Zicntr/mcountinhibit.layout",
  __FILE__
] do |t|
  puts "Generating #{Pathname.new(t.name).relative_path_from($root)}"
  erb = ERB.new(File.read($root / "arch/csr/Zicntr/mcountinhibit.layout"), trim_mode: "-")
  erb.filename = "#{$root}/arch/csr/Zicntr/mcountinhibit.layout"
  File.write(t.name, insert_warning(erb.result(binding), t.prerequisites.first))
end

namespace :gen do
  desc "Generate architecture files from layouts"
  task :arch do
    (3..31).each do |hpm_num|
      Rake::Task["#{$root}/arch/csr/Zihpm/mhpmcounter#{hpm_num}.yaml"].invoke
      Rake::Task["#{$root}/arch/csr/Zihpm/mhpmcounter#{hpm_num}h.yaml"].invoke
      Rake::Task["#{$root}/arch/csr/Zihpm/mhpmevent#{hpm_num}.yaml"].invoke
      Rake::Task["#{$root}/arch/csr/Zihpm/mhpmevent#{hpm_num}h.yaml"].invoke

      Rake::Task["#{$root}/arch/csr/Zihpm/hpmcounter#{hpm_num}.yaml"].invoke
      Rake::Task["#{$root}/arch/csr/Zihpm/hpmcounter#{hpm_num}h.yaml"].invoke
    end

    Rake::Task["#{$root}/arch/csr/I/mcounteren.yaml"].invoke
    Rake::Task["#{$root}/arch/csr/S/scounteren.yaml"].invoke
    Rake::Task["#{$root}/arch/csr/H/hcounteren.yaml"].invoke
    Rake::Task["#{$root}/arch/csr/Zicntr/mcountinhibit.yaml"].invoke

    (0..63).each do |pmpaddr_num|
      Rake::Task["#{$root}/arch/csr/I/pmpaddr#{pmpaddr_num}.yaml"].invoke
    end

    (0..15).each do |pmpcfg_num|
      Rake::Task["#{$root}/arch/csr/I/pmpcfg#{pmpcfg_num}.yaml"].invoke
    end
  end
end

namespace :test do
  desc <<~DESC
    Run smoke tests

    These are basic but fast-running tests to check the database and tools
  DESC
  task :smoke do
    Rake::Task["test:idl_compiler"].invoke
    Rake::Task["test:lib"].invoke
    Rake::Task["test:schema"].invoke
    Rake::Task["test:idl_model"].invoke
  end

  desc <<~DESC
    Run the regression tests

    These tests must pass before a commit will be allowed in the main branch on GitHub
  DESC
  task :regress do
    Rake::Task["test:smoke"].invoke

    ENV["MANUAL_NAME"] = "isa"
    ENV["VERSIONS"] = "all"
    Rake::Task["gen:html_manual"].invoke
    
    ENV["EXT"] = "B"
    ENV["VERSION"] = "latest"
    Rake::Task["gen:ext_pdf"].invoke

    Rake::Task["gen:html"].invoke("generic_rv64")

    Rake::Task["#{$root}/gen/certificate_doc/pdf/MockCertificateModel.pdf"].invoke
    Rake::Task["#{$root}/gen/profile_doc/pdf/MockProfileRelease.pdf"].invoke

    puts
    puts "Regression test PASSED"
  end

  desc <<~DESC
    Run the nightly regression tests

    Generally, this tries to build all artifacts
  DESC
  task :nightly do
    Rake::Task["regress"].invoke

    Rake::Task["#{$root}/gen/certificate_doc/pdf/MC100.pdf"].invoke
    Rake::Task["#{$root}/gen/profile_doc/pdf/RVA20.pdf"].invoke
    Rake::Task["#{$root}/gen/profile_doc/pdf/RVA22.pdf"].invoke
    Rake::Task["#{$root}/gen/profile_doc/pdf/RVI20.pdf"].invoke

    puts
    puts "Nightly regression test PASSED"
  end
end

namespace :gen do
  desc <<~DESC
    Generate all certificates and profile PDFs.
  DESC
  task :cert_profile_pdfs do
    puts "==================================="
    puts "cert_profile_pdfs: Generating MC100"
    puts "                   1st target"
    puts "==================================="
    Rake::Task["#{$root}/gen/certificate_doc/pdf/MC100.pdf"].invoke

    puts "=================================================="
    puts "cert_profile_pdfs: Generating MockCertificateModel"
    puts "                   2nd target"
    puts "=================================================="
    Rake::Task["#{$root}/gen/certificate_doc/pdf/MockCertificateModel.pdf"].invoke

    puts "==================================="
    puts "cert_profile_pdfs: Generating RVA20"
    puts "                   3rd target"
    puts "==================================="
    Rake::Task["#{$root}/gen/profile_doc/pdf/RVA20.pdf"].invoke

    puts "==================================="
    puts "cert_profile_pdfs: Generating RVA22"
    puts "                   4th target"
    puts "==================================="
    Rake::Task["#{$root}/gen/profile_doc/pdf/RVA22.pdf"].invoke

    puts "==================================="
    puts "cert_profile_pdfs: Generating RVI20"
    puts "                   5th target"
    puts "==================================="
    Rake::Task["#{$root}/gen/profile_doc/pdf/RVI20.pdf"].invoke

    puts "==================================="
    puts "cert_profile_pdfs: Generating MockProfileRelease"
    puts "                   6th target"
    puts "==================================="
    Rake::Task["#{$root}/gen/profile_doc/pdf/MockProfileRelease.pdf"].invoke
  end
end