module Jekyll
  module WebPFilter
    # Konvertiert einen Bildpfad zu WebP
    def to_webp(input)
      return input if input.nil? || input.empty?
      ext = File.extname(input)
      input.sub(ext, '.webp')
    end
  end
end

Liquid::Template.register_filter(Jekyll::WebPFilter)