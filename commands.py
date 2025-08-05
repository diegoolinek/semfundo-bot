import discord
from discord.ext import commands
from rembg import remove
from PIL import Image
from io import BytesIO
import asyncio

class RemoveBackground(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='semfundo', help='Remove o fundo de uma imagem.')
    async def semfundo(self, ctx):
        if len(ctx.message.attachments) > 0:
            for attachment in ctx.message.attachments:
                if attachment.content_type.startswith('image/'):
                    processing_message = await ctx.send("Processando sua imagem, aguarde...")
                    try:
                        image_data = await attachment.read()

                        if len(image_data) > 8000000:
                            await ctx.send("Desculpe, o arquivo é muito grande. O limite é de 8MB.")
                            return
                        
                        input_image = Image.open(BytesIO(image_data))
                        output_image = remove(input_image)
                        
                        output_buffer = BytesIO()
                        output_image.save(output_buffer, 'PNG')
                        output_buffer.seek(0)
                        
                        embed = discord.Embed(
                            title="Fundo Removido!",
                            description="Sua imagem está pronta.",
                            color=discord.Color.green()
                        )
                        file = discord.File(output_buffer, filename='semfundo.png')
                        embed.set_image(url=f"attachment://semfundo.png")
                        embed.set_footer(text=f"Processado por {self.bot.user.name}")
                        await ctx.send(file=file, embed=embed)
                        
                        await processing_message.delete()
                    except asyncio.TimeoutError:
                        await ctx.send("O processamento da imagem demorou demais e falhou. Tente uma imagem menor.")
                    except Exception as e:
                        await ctx.send(f"Ocorreu um erro ao processar a imagem. Erro: {e}")
                else:
                    await ctx.send("Por favor, envie um arquivo de imagem válido.")
        else:
            await ctx.send("Você precisa enviar uma imagem com o comando `!semfundo`.")

    @commands.command(name='pb', help='Converte uma imagem para preto e branco.')
    async def preto_e_branco(self, ctx):
        if len(ctx.message.attachments) > 0:
            for attachment in ctx.message.attachments:
                if attachment.content_type.startswith('image/'):
                    processing_message = await ctx.send("Convertendo sua imagem para preto e branco, aguarde...")
                    try:
                        image_data = await attachment.read()

                        if len(image_data) > 8000000:
                            await ctx.send("Desculpe, o arquivo é muito grande. O limite é de 8MB.")
                            return

                        input_image = Image.open(BytesIO(image_data))
                        output_image = input_image.convert("L")
                        output_buffer = BytesIO()
                        output_image.save(output_buffer, 'PNG')
                        output_buffer.seek(0)
                        
                        embed = discord.Embed(
                            title="Imagem Convertida!",
                            description="Sua imagem está agora em preto e branco.",
                            color=discord.Color.blue()
                        )
                        
                        file = discord.File(output_buffer, filename='preto_e_branco.png')
                        embed.set_image(url=f"attachment://preto_e_branco.png")
                        embed.set_footer(text=f"Processado por {self.bot.user.name}")
                        await ctx.send(file=file, embed=embed)

                        await processing_message.delete()
                    except asyncio.TimeoutError:
                        await ctx.send("O processamento da imagem demorou demais e falhou. Tente uma imagem menor.")
                    except Exception as e:
                        await ctx.send(f"Ocorreu um erro ao converter a imagem. Erro: {e}")
                else:
                    await ctx.send("Por favor, envie um arquivo de imagem válido.")
        else:
            await ctx.send("Você precisa enviar uma imagem com o comando `!pb`.")

    @commands.command(name='ajuda')
    async def ajuda(self, ctx):
        """Mostra todos os comandos disponíveis."""
        embed = discord.Embed(
            title="Comandos do Bot",
            description="Use `!` seguido de um comando e anexe sua imagem para processá-la.",
            color=discord.Color.blue()
        )
        
        for command in self.bot.commands:
            if not command.hidden and command.name != "ajuda":
                embed.add_field(
                    name=f"`!{command.name}`",
                    value=command.help or "Sem descrição.",
                    inline=False
                )
        
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(RemoveBackground(bot))
