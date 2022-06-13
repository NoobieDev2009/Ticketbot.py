from optparse import Option
from pickle import TRUE
from pydoc import describe
import discord
from discord import *
from discord import member
import discord.ext.commands as commands
from discord import message
from discord.ext import tasks, commands
from discord.ext.commands import cooldown, BucketType
from discord.ext.commands import Bot
import datetime
from datetime import date
import asyncio
import traceback
import requests
import os.path
import re
import aiohttp
import random
import os
import time
import sys
from discord.utils import get
from time import sleep
from discord.ext import commands
from discord.ext import *
from json import load
from pathlib import Path
import subprocess, threading, discord, asyncio, random, ctypes, re, os
import functools

with Path("config.json").open() as f:
    config = load(f)
   @bot.command()
async def ticket(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> {prefix}ticket')
    if ctx.channel.type != discord.ChannelType.private:
        channels = [str(x) for x in bot.get_all_channels()]
        if f'ticket-{ctx.author}' in str(channels):
            embed = discord.Embed(color=0xFCFCFC, description='You already have a ticket open!')
            await ctx.send(embed=embed)
        else:
            ticket_channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.id}')
            await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)
            await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
            embed = discord.Embed(color=0xFCFCFC, description=f'Please enter the reason for this ticket, type `{prefix}close` if you want to close this ticket.')
            await ticket_channel.send(f'{ctx.author.mention}', embed=embed)
            

@bot.command()
async def close(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> {prefix}close')
    if ctx.channel.type != discord.ChannelType.private:
        if ctx.channel.name == f'ticket-{ctx.author.id}':
            await ctx.channel.delete()
        elif ctx.author.id in administrators and 'ticket' in ctx.channel.name:
            await ctx.channel.delete()
        else:
            embed = discord.Embed(color=0xFCFCFC, description=f'You do not have permission to run this command!')
            await ctx.send(embed=embed)

token = config["Token"]
prefix = config["Prefix"]

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)
bot.remove_command('help')

@bot.event()
async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
@bot.command()
async def ticket(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> {prefix}ticket')
    if ctx.channel.type != discord.ChannelType.private:
        channels = [str(x) for x in bot.get_all_channels()]
        if f'ticket-{ctx.author}' in str(channels):
            embed = discord.Embed(color=0xFCFCFC, description='You already have a ticket open!')
            await ctx.send(embed=embed)
        else:
            ticket_channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.id}')
            await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)
            await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
            embed = discord.Embed(color=0xFCFCFC, description=f'Please enter the reason for this ticket, type `{prefix}close` if you want to close this ticket.')
            await ticket_channel.send(f'{ctx.author.mention}', embed=embed)
            

@bot.command()
async def close(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> {prefix}close')
    if ctx.channel.type != discord.ChannelType.private:
        if ctx.channel.name == f'ticket-{ctx.author.id}':
            await ctx.channel.delete()
        elif ctx.author.id in administrators and 'ticket' in ctx.channel.name:
            await ctx.channel.delete()
        else:
            embed = discord.Embed(color=0xFCFCFC, description=f'You do not have permission to run this command!')
            await ctx.send(embed=embed)
 bot.run(token)
