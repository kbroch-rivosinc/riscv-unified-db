# frozen_string_literal: true
#
# Collection of "helper" functions that can be called from ERB templates.

require "erb"
require "pathname"

module TemplateHelpers
  # Insert a hyperlink to an extension.
  # @param name [#to_s] Name of the extension
  def link_to_ext(name)
    "%%LINK%ext;#{name};#{name}%%"
  end

  # Insert a hyperlink to an extension parameter.
  # @param ext_name [#to_s] Name of the extension
  # @param param_name [#to_s] Name of the parameter
  def link_to_ext_param(ext_name, param_name)
    "<<ext-#{ext_name.gsub(".", "_")}-param-#{param_name}-def, #{ext_name}>>"
  end

  # Insert a hyperlink to an instruction.
  # @param name [#to_s] Name of the instruction
  def link_to_inst(name)
    "%%LINK%inst;#{name};#{name}%%"
  end

  # Insert a hyperlink to a CSR.
  # @param name [#to_s] Name of the CSR
  def link_to_csr(name)
    "%%LINK%csr;#{name};#{name}%%"
  end

  # Insert a hyperlink to a CSR field.
  # @param csr_name [#to_s] Name of the CSR
  # @param field_name [#to_s] Name of the CSR field
  def link_to_csr_field(csr_name, field_name)
    "%%LINK%csr_field;#{csr_name}.#{field_name};#{csr_name}.#{field_name}%%"
  end

  # Insert anchor to an extension.
  # @param name [#to_s] Name of the extension
  def anchor_for_ext(name)
    "[[ext-#{name.gsub(".", "_")}-def]]"
  end

  # Insert anchor to an extension parameter.
  # @param ext_name [#to_s] Name of the extension
  # @param param_name [#to_s] Name of the parameter
  def anchor_for_ext_param(ext_name, param_name)
    "[[ext-#{ext_name.gsub(".", "_")}-param-#{param_name}-def]]"
  end

  # Insert anchor to an instruction.
  # @param name [#to_s] Name of the instruction
  def anchor_for_inst(name)
    "[[inst-#{name.gsub(".", "_")}-def]]"
  end

  # Insert anchor to a CSR.
  # @param name [#to_s] Name of the CSR
  def anchor_for_csr(name)
    "[[csr-#{name.gsub(".", "_")}-def]]"
  end

  # Insert anchor to a CSR field.
  # @param csr_name [#to_s] Name of the CSR
  # @param field_name [#to_s] Name of the CSR field
  def anchor_for_csr_field(csr_name, field_name)
    "[[csr_field-#{csr_name.gsub(".", "_")}-#{field_name.gsub(".", "_")}-def]]"
  end

  # Include a partial ERB template into a full ERB template.
  #
  # @param template_pname [String] Path to template file relative to backends directory
  # @param inputs [Hash<String, Object>] Input objects to pass into template
  # @return [String] Result of ERB evaluation of the template file
  def partial(template_pname, inputs = {})
    template_path = Pathname.new($root / "backends" / template_pname)
    raise ArgumentError, "Template '#{template_path} not found" unless template_path.exist?

    erb = ERB.new(template_path.read, trim_mode: "-")
    erb.filename = template_path.realpath.to_s

    erb.result(OpenStruct.new(inputs).instance_eval { binding })
  end
end
